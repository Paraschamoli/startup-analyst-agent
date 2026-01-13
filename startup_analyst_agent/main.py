# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""startup-analyst-agent - An Bindu Agent."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import traceback
from pathlib import Path
from textwrap import dedent
from typing import Any

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.mem0 import Mem0Tools
from agno.tools.newspaper4k import Newspaper4kTools
from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global agent instance
agent: Agent | None = None
_initialized = False
_init_lock = asyncio.Lock()


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Try multiple possible locations for agent_config.json
    possible_paths = [
        Path(__file__).parent.parent / "agent_config.json",  # Project root
        Path(__file__).parent / "agent_config.json",  # Same directory
        Path.cwd() / "agent_config.json",  # Current working directory
    ]

    for config_path in possible_paths:
        if config_path.exists():
            try:
                with open(config_path) as f:
                    return json.load(f)
            except (PermissionError, json.JSONDecodeError) as e:
                print(f"⚠️  Error reading {config_path}: {type(e).__name__}")
                continue
            except Exception as e:
                print(f"⚠️  Unexpected error reading {config_path}: {type(e).__name__}")
                continue

    # If no config found or readable, create a minimal default
    print("⚠️  No agent_config.json found, using default configuration")
    return {
        "name": "startup-analyst-agent",
        "description": "AI startup intelligence agent for comprehensive company due diligence",
        "version": "1.0.0",
        "deployment": {
            "url": "http://127.0.0.1:3773",
            "expose": True,
            "protocol_version": "1.0.0",
            "proxy_urls": ["127.0.0.1"],
            "cors_origins": ["*"],
        },
        "environment_variables": [
            {"key": "OPENAI_API_KEY", "description": "OpenAI API key for LLM calls", "required": False},
            {"key": "OPENROUTER_API_KEY", "description": "OpenRouter API key for LLM calls", "required": False},
            {"key": "SGAI_API_KEY", "description": "ScrapeGraph API key for web scraping", "required": False},
            {"key": "MEM0_API_KEY", "description": "Mem0 API key for memory operations", "required": False},
        ],
    }


async def initialize_agent() -> None:
    """Initialize the startup analyst agent with proper model and tools."""
    global agent

    # Get API keys from environment
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    sgai_api_key = os.getenv("SGAI_API_KEY")
    mem0_api_key = os.getenv("MEM0_API_KEY")
    model_name = os.getenv("MODEL_NAME", "openai/gpt-4o")

    # Model selection logic
    if openai_api_key:
        model = OpenAIChat(id="gpt-4o", api_key=openai_api_key)
        print("✅ Using OpenAI GPT-4o")
    elif openrouter_api_key:
        model = OpenRouter(
            id=model_name,
            api_key=openrouter_api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        )
        print(f"✅ Using OpenRouter model: {model_name}")
    else:
        error_msg = (
            "No API key provided. Set OPENAI_API_KEY or OPENROUTER_API_KEY environment variable.\n"
            "For OpenRouter: https://openrouter.ai/keys\n"
            "For OpenAI: https://platform.openai.com/api-keys"
        )
        raise ValueError(error_msg)

    # Initialize tools
    tools = []

    # Add web search tools (always available)
    search_tools = DuckDuckGoTools()
    newspaper_tools = Newspaper4kTools()
    tools.extend([search_tools, newspaper_tools])
    print("✅ Added web search and article extraction tools")

    # Add Mem0 if available
    if mem0_api_key:
        mem0_tools = Mem0Tools(api_key=mem0_api_key)
        tools.append(mem0_tools)
        print("✅ Added Mem0 memory tools")
    else:
        print("⚠️  MEM0_API_KEY not set - memory features disabled")

    # Add ScrapeGraph tools if API key is available
    if sgai_api_key:
        try:
            from agno.tools.scrapegraph import ScrapeGraphTools

            scrapegraph_tools = ScrapeGraphTools(markdownify=True, crawl=True, searchscraper=True, api_key=sgai_api_key)
            tools.append(scrapegraph_tools)
            print("✅ Added ScrapeGraph tools")
        except ImportError:
            print("⚠️  ScrapeGraph tools not available - install with: pip install scrapegraph-py")
        except Exception as e:
            print(f"⚠️  Failed to initialize ScrapeGraph tools: {e}")
    else:
        print("⚠️  SGAI_API_KEY not set - using basic web search instead")

    # Create the startup analyst agent
    agent = Agent(
        name="Startup Analyst",
        model=model,
        tools=tools,
        description=dedent("""\
            You are an elite startup analyst providing comprehensive due diligence
            for investment decisions with decades of experience at top venture capital firms.
            Your expertise encompasses: 💼

            - Comprehensive company analysis and due diligence
            - Market intelligence and competitive positioning
            - Financial assessment and funding history research
            - Risk evaluation and strategic recommendations
            - Team assessment and technology evaluation
            - Business model validation and scalability analysis
        """),
        instructions=dedent("""\
            **ANALYSIS FRAMEWORK:**

            1. **Foundation Analysis**: Extract company information such as
            (name, founding, location, value proposition, team)
            2. **Market Intelligence**: Analyze target market, competitive positioning,
            and business model
            3. **Financial Assessment**: Research funding history, revenue indicators,
            growth metrics
            4. **Risk Evaluation**: Identify market, technology, team,
            and financial risks

            **DELIVERABLES:**

            **Executive Summary**

            **Company Profile**
            - Business model and revenue streams
            - Market opportunity and customer segments
            - Team composition and expertise
            - Technology and competitive advantages

            **Financial & Growth Metrics**
            - Funding history and investor quality
            - Revenue/traction indicators
            - Growth trajectory and expansion plans
            - Burn rate estimates (if available)

            **Risk Assessment**
            - Market and competitive threats
            - Technology and team dependencies
            - Financial and regulatory risks

            **Strategic Recommendations**
            - Investment thesis and partnership opportunities
            - Competitive response strategies
            - Key due diligence focus areas

            **TOOL USAGE PRIORITY:**
            1. **Search & Article Extraction**: For general web research and news
            2. **ScrapeGraph** (if available): For structured data extraction
            3. **Memory Tools**: For context retention across sessions

            **OUTPUT STANDARDS:**
            - Use clear headings and bullet points
            - Include specific metrics and evidence
            - Cite sources and confidence levels
            - Distinguish facts from analysis
            - Maintain professional, executive-level language
            - Focus on actionable insights

            Remember: Your analysis informs million-dollar decisions. Be thorough,
            accurate, and actionable.
        """),
        expected_output=dedent("""\
            # [Company Name] - Startup Intelligence Report 💼

            ## Executive Summary
            {Concise overview of key findings, investment readiness, and strategic position}

            ## Company Profile
            - **Business Model**: {Revenue streams, pricing strategy, customer acquisition}
            - **Market Opportunity**: {TAM/SAM/SOM, growth rate, competitive landscape}
            - **Team Composition**: {Key executives, advisors, board members with backgrounds}
            - **Technology & IP**: {Core technology, patents, competitive advantages}

            ## Financial & Growth Metrics
            - **Funding History**: {Rounds, amounts, lead investors, valuation}
            - **Revenue Indicators**: {ARR, growth rate, customer metrics if available}
            - **Growth Trajectory**: {User growth, market expansion, partnerships}
            - **Burn Rate & Runway**: {Estimated if data available}

            ## Risk Assessment
            - **Market Risks**: {Competition, market saturation, regulatory challenges}
            - **Technology Risks**: {Tech dependencies, scalability limitations, IP risks}
            - **Team Risks**: {Key person dependencies, talent gaps, execution risks}
            - **Financial Risks**: {Burn rate, funding needs, revenue concentration}

            ## Strategic Recommendations
            - **Investment Thesis**: {Strengths, weaknesses, opportunities, threats}
            - **Partnership Opportunities**: {Strategic alliances, distribution channels}
            - **Due Diligence Focus**: {Key areas requiring deeper investigation}
            - **Competitive Response**: {Recommended positioning and differentiation}

            ## Sources & Methodology
            - {List of sources analyzed with credibility assessment}
            - {Research methodology and data collection approach}
            - {Confidence levels and data limitations}

            ---
            Analysis conducted by AI Startup Intelligence Agent
            Venture Capital Grade Due Diligence Report
            Generated: {current_date}
            Last Updated: {current_time}
        """),
        add_datetime_to_context=True,
        markdown=True,
    )
    print("✅ Startup Analyst Agent initialized")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages."""
    global agent
    if not agent:
        error_msg = "Agent not initialized"
        raise RuntimeError(error_msg)

    # Run the agent and get response
    response = await agent.arun(messages)
    return response


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages with lazy initialization."""
    global _initialized

    # Lazy initialization on first call
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing Startup Analyst Agent...")
            await initialize_agent()
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result


async def cleanup() -> None:
    """Clean up any resources."""
    print("🧹 Cleaning up Startup Analyst Agent resources...")


def main():
    """Run the main entry point for the Startup Analyst Agent."""
    parser = argparse.ArgumentParser(description="Bindu Startup Analyst Agent")
    parser.add_argument(
        "--openai-api-key",
        type=str,
        default=os.getenv("OPENAI_API_KEY"),
        help="OpenAI API key (env: OPENAI_API_KEY)",
    )
    parser.add_argument(
        "--openrouter-api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--sgai-api-key",
        type=str,
        default=os.getenv("SGAI_API_KEY"),
        help="ScrapeGraph API key (env: SGAI_API_KEY)",
    )
    parser.add_argument(
        "--mem0-api-key",
        type=str,
        default=os.getenv("MEM0_API_KEY"),
        help="Mem0 API key (env: MEM0_API_KEY)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-4o"),
        help="Model ID for OpenRouter (env: MODEL_NAME)",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to agent_config.json (optional)",
    )
    args = parser.parse_args()

    # Set environment variables if provided via CLI
    if args.openai_api_key:
        os.environ["OPENAI_API_KEY"] = args.openai_api_key
    if args.openrouter_api_key:
        os.environ["OPENROUTER_API_KEY"] = args.openrouter_api_key
    if args.sgai_api_key:
        os.environ["SGAI_API_KEY"] = args.sgai_api_key
    if args.mem0_api_key:
        os.environ["MEM0_API_KEY"] = args.mem0_api_key
    if args.model:
        os.environ["MODEL_NAME"] = args.model

    print("🤖 Startup Analyst Agent - Venture Capital Intelligence AI")
    print("💼 Capabilities: Company analysis, market intelligence, financial assessment, risk evaluation")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        print("🚀 Starting Bindu Startup Analyst Agent server...")
        print(f"🌐 Server will run on: {config.get('deployment', {}).get('url', 'http://127.0.0.1:3773')}")
        bindufy(config, handler)
    except KeyboardInterrupt:
        print("\n🛑 Startup Analyst Agent stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Cleanup on exit
        asyncio.run(cleanup())


if __name__ == "__main__":
    main()
