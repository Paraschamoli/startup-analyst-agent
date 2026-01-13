<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">Startup Analyst Agent</h1>
<h3 align="center">AI-Powered Venture Capital Intelligence Assistant</h3>

<p align="center">
  <strong>Professional startup analysis agent combining market research with venture capital due diligence</strong><br/>
  Comprehensive company analysis, financial assessment, risk evaluation, and investment recommendations powered by AI
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/startup-analyst-agent/actions/workflows/build-and-push.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/startup-analyst-agent/build-and-push.yml?branch=main" alt="Build Status">
  </a>
  <a href="https://pypi.org/project/startup-analyst-agent/">
    <img src="https://img.shields.io/pypi/v/startup-analyst-agent" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python Version">
  <a href="https://github.com/Paraschamoli/startup-analyst-agent/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Paraschamoli/startup-analyst-agent" alt="License">
  </a>
</p>

---

## 🎯 What is Startup Analyst Agent?

An AI-powered business intelligence assistant that provides comprehensive due diligence and startup analysis for investment decisions. Think of it as having a top-tier venture capital analyst available 24/7.

### Key Features
*   **🔍 Company Analysis** - Deep due diligence on business models and market positioning
*   **📊 Financial Assessment** - Funding history, revenue indicators, and growth metrics
*   **🧠 Market Intelligence** - Competitive landscape analysis and opportunity sizing
*   **⚠️ Risk Evaluation** - Comprehensive risk assessment across multiple dimensions
*   **💼 Strategic Recommendations** - Data-driven investment theses and recommendations
*   **⚡ Lazy Initialization** - Fast boot times, initializes on first request
*   **🔐 Secure API Handling** - No API keys required at startup

---

## 🛠️ Tools & Capabilities

### Built-in Tools
*   **DuckDuckGoTools** - Real-time web search for market research
*   **Newspaper4kTools** - Article parsing and content extraction
*   **ScrapeGraphTools** - Enhanced web scraping for structured data (optional)
*   **Mem0Tools** - Memory and context retention (optional)

### Analysis Framework
1.  **Foundation Analysis** - Company information, team, value proposition
2.  **Market Intelligence** - Target market, competitive positioning, business model
3.  **Financial Assessment** - Funding history, revenue indicators, growth metrics
4.  **Risk Evaluation** - Market, technology, team, and financial risks
5.  **Strategic Recommendations** - Investment thesis and actionable insights

---

> **🌐 Join the Internet of Agents**
> Register your agent at [bindus.directory](https://bindus.directory) to make it discoverable worldwide and enable agent-to-agent collaboration. It takes 2 minutes and unlocks the full potential of your agent.

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/startup-analyst-agent.git
cd startup-analyst-agent

# Set up virtual environment with uv
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API key (choose one):
# OPENAI_API_KEY=sk-...      # For OpenAI GPT-4o
# OPENROUTER_API_KEY=sk-...  # For OpenRouter (cheaper alternative)
# SGAI_API_KEY=sk-...        # For enhanced scraping (optional)
# MEM0_API_KEY=sk-...        # For memory features (optional)
```

### 3. Run Locally

```bash
# Start the startup analyst agent
python -m startup_analyst_agent

# Or using uv
uv run python -m startup_analyst_agent
```

### 4. Test with Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access at: http://localhost:3773
```

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file:

```env
# Choose ONE provider (both can be set, OpenAI takes priority)
OPENAI_API_KEY=sk-...      # OpenAI API key
OPENROUTER_API_KEY=sk-...  # OpenRouter API key (alternative)

# Optional - for enhanced features
SGAI_API_KEY=sk-...        # ScrapeGraph API key for enhanced scraping
MEM0_API_KEY=sk-...        # Mem0 API key for memory operations

# Optional
DEBUG=true                # Enable debug logging
MODEL_NAME=openai/gpt-4o  # Model override
```

### Port Configuration
Default port: `3773` (can be changed in `agent_config.json`)

---

## 💡 Usage Examples

### Via HTTP API

```bash
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Perform comprehensive due diligence on Tesla as a startup investment opportunity. Analyze business model, market positioning, financial metrics, competitive landscape, and investment risks."
      }
    ]
  }'
```

### Sample Startup Analysis Query

```text
"Analyze OpenAI as a startup investment opportunity.
Include: business model evolution, market opportunity in AI, competitive advantages,
funding history, revenue streams, key risks, and investment recommendation."

"Evaluate Stripe's position in the fintech market.
Focus on: market share, competitive differentiation, growth metrics,
international expansion challenges, and strategic opportunities."

"Provide a SWOT analysis for SpaceX covering:
technology advantages, market opportunity in space industry,
funding challenges, regulatory risks, and competitive landscape."
```

### Expected Output Format

```markdown
# [Company Name] - Startup Intelligence Report 💼

## Executive Summary
Concise overview of key findings, investment readiness, and strategic position...

## Company Profile
- **Business Model**: Revenue streams, pricing strategy, customer acquisition
- **Market Opportunity**: TAM/SAM/SOM, growth rate, competitive landscape
- **Team Composition**: Key executives, advisors, board members with backgrounds
- **Technology & IP**: Core technology, patents, competitive advantages

## Financial & Growth Metrics
- **Funding History**: Rounds, amounts, lead investors, valuation
- **Revenue Indicators**: ARR, growth rate, customer metrics if available
- **Growth Trajectory**: User growth, market expansion, partnerships
- **Burn Rate & Runway**: Estimated if data available

## Risk Assessment
- **Market Risks**: Competition, market saturation, regulatory challenges
- **Technology Risks**: Tech dependencies, scalability limitations, IP risks
- **Team Risks**: Key person dependencies, talent gaps, execution risks
- **Financial Risks**: Burn rate, funding needs, revenue concentration

## Strategic Recommendations
- Investment thesis and partnership opportunities
- Competitive response strategies
- Key due diligence focus areas

## Sources & Methodology
List of sources analyzed with credibility assessment...
```

---

## 🐳 Docker Deployment

### Quick Docker Setup

```bash
# Build the image
docker build -t startup-analyst-agent .

# Run container
docker run -d \
  -p 3773:3773 \
  -e OPENAI_API_KEY=your_key_here \
  --name startup-analyst-agent \
  startup-analyst-agent

# Check logs
docker logs -f startup-analyst-agent
```

### Docker Compose (Recommended)
`docker-compose.yml`

```yaml
version: '3.8'
services:
  startup-analyst-agent:
    build: .
    ports:
      - "3773:3773"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - SGAI_API_KEY=${SGAI_API_KEY}
      - MEM0_API_KEY=${MEM0_API_KEY}
    restart: unless-stopped
```

Run with Compose:
```bash
# Start with compose
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 📁 Project Structure

```text
startup-analyst-agent/
├── startup_analyst_agent/
│   ├── __init__.py          # Package initialization
│   ├── __version__.py       # Version information
│   └── main.py              # Main agent implementation
├── skills/
│   └── startup-analyst/
│       └── skill.yaml       # Skill configuration
├── agent_config.json        # Bindu agent configuration
├── pyproject.toml           # Python dependencies
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # Docker Compose setup
├── README.md                # This documentation
├── .env.example             # Environment template
└── uv.lock                  # Dependency lock file
```

---

## 🔌 API Reference

### Health Check
```bash
GET http://localhost:3773/health
```
Response:
```json
{"status": "healthy", "agent": "Startup Analyst Agent"}
```

### Chat Endpoint
```bash
POST http://localhost:3773/chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "Your startup analysis query here"}
  ]
}
```

### Agent Information
```bash
GET http://localhost:3773/agent/info
```

---

## 🧪 Testing

### Local Testing

```bash
# Install test dependencies
uv sync --group dev

# Run tests
pytest tests/

# Test with specific API key
OPENAI_API_KEY=test_key python -m pytest
```

### Integration Test

```bash
# Start agent
python -m startup_analyst_agent &

# Test API endpoint
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Analyze Tesla as a startup investment"}]}'
```

---

## 🚨 Troubleshooting

### Common Issues & Solutions

**"ModuleNotFoundError"**
```bash
uv sync --force
```

**"Port 3773 already in use"**
Change port in `agent_config.json` or kill the process:
```bash
lsof -ti:3773 | xargs kill -9
```

**"No API key provided"**
Check if `.env` exists and variable names match. Or set directly:
```bash
export OPENAI_API_KEY=your_key
```

**"ScrapeGraph tools not available"**
Install optional dependency:
```bash
pip install scrapegraph-py
```

**Docker build fails**
```bash
docker system prune -a
docker-compose build --no-cache
```

---

## 📊 Dependencies

### Core Packages
*   **bindu** - Agent deployment framework
*   **agno** - AI agent framework
*   **openai** - OpenAI client
*   **requests** - HTTP requests
*   **rich** - Console output
*   **duckduckgo-search** - Web search
*   **newspaper4k** - Article parsing
*   **python-dotenv** - Environment management
*   **scrapegraph-py** - Enhanced web scraping (optional)
*   **mem0ai** - Memory operations (optional)

### Development Packages
*   **pytest** - Testing framework
*   **ruff** - Code formatting/linting
*   **pre-commit** - Git hooks

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1.  Fork the repository
2.  Create a feature branch: `git checkout -b feature/improvement`
3.  Make your changes following the code style
4.  Add tests for new functionality
5.  Commit with descriptive messages
6.  Push to your fork
7.  Open a Pull Request

**Code Style:**
*   Follow PEP 8 conventions
*   Use type hints where possible
*   Add docstrings for public functions
*   Keep functions focused and small

---

## 📄 License
MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Credits & Acknowledgments
*   **Developer:** Paras Chamoli
*   **Framework:** Bindu - Agent deployment platform
*   **Agent Framework:** Agno - AI agent toolkit
*   **Search Tools:** DuckDuckGo Search API
*   **Content Parsing:** Newspaper4k library
*   **Enhanced Scraping:** ScrapeGraph toolkit

### 🔗 Useful Links
*   🌐 **Bindu Directory:** [bindus.directory](https://bindus.directory)
*   📚 **Bindu Docs:** [docs.getbindu.com](https://docs.getbindu.com)
*   🐙 **GitHub:** [github.com/Paraschamoli/startup-analyst-agent](https://github.com/Paraschamoli/startup-analyst-agent)
*   💬 **Discord:** Bindu Community

---

<p align="center">
  <strong>Built with ❤️ by Paras Chamoli</strong><br/>
  <em>Transforming startup analysis with AI-powered venture capital intelligence</em>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/startup-analyst-agent/stargazers">⭐ Star on GitHub</a> •
  <a href="https://bindus.directory">🌐 Register on Bindu</a> •
  <a href="https://github.com/Paraschamoli/startup-analyst-agent/issues">🐛 Report Issues</a>
</p>

> **Note:** This agent follows the Bindu pattern with lazy initialization and secure API key handling. It boots without API keys and only fails at runtime if keys are needed but not provided.
