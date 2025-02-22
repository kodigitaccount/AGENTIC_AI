from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Fetch OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure API key is set
if not openai_api_key:
    raise ValueError("Missing OpenAI API Key. Set OPENAI_API_KEY in your .env file.")

# Web Agent
web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),  # Explicit API key
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Combined Agent Team
agent_team = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Run Query
agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)
