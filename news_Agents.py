"""Run `pip install phi` to install dependencies."""

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo  # For fetching news
from dotenv import load_dotenv

# Load environment variables (e.g., API keys)
load_dotenv()

# ✅ News Agent (Fetches latest financial news)
news_agent = Agent(
    name="News Agent",
    model=Groq(id="llama-3.3-70b-versatile"),  # AI model for processing news
    tools=[DuckDuckGo()],  # Uses DuckDuckGo to fetch news
    instructions=[
        "Search for the latest financial news about the given company.",
        "Summarize the top news articles.",
        "Provide key insights in markdown format for readability."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Run Query to Fetch Financial News
news_agent.print_response(
    "Find and summarize the latest financial news about Tesla and NVIDIA.", 
    stream=True
)
