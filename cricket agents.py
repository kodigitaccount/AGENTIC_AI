from phi.agent import Agent
from phi.model.openai import OpenAIChat  # Using OpenAI's API
from phi.tools.duckduckgo import DuckDuckGo  # For fetching live cricket data
from dotenv import load_dotenv
import os

# Load API keys
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # Ensure this is set in your environment

# ✅ Live Cricket Match Agent
match_agent = Agent(
    name="Live Match Agent",
    model=OpenAIChat(id="gpt-4o", api_key=api_key),  # Using OpenAI GPT-4o
    tools=[DuckDuckGo()],
    instructions=[
        "Search for live cricket match scores.",
        "Summarize the score, top players, and match situation.",
        "Use markdown tables for clarity."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Player Stats Agent
player_agent = Agent(
    name="Player Stats Agent",
    model=OpenAIChat(id="gpt-4o", api_key=api_key),
    tools=[DuckDuckGo()],
    instructions=[
        "Find recent cricket player statistics.",
        "Include batting and bowling stats for the last 5 matches.",
        "Use tables for formatting."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Cricket News Agent
news_agent = Agent(
    name="Cricket News Agent",
    model=OpenAIChat(id="gpt-4o", api_key=api_key),
    tools=[DuckDuckGo()],
    instructions=[
        "Find and summarize the latest cricket news.",
        "Highlight upcoming matches, injuries, and tournament updates.",
        "List headlines with sources."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Main Cricket Team (Combining all agents)
cricket_team = Agent(
    name="Cricket Analysis Team",
    model=OpenAIChat(id="gpt-4o", api_key=api_key),
    team=[match_agent, player_agent, news_agent],
    instructions=[
        "Provide live match scores, player statistics, and news updates.",
        "Use structured formatting and markdown tables.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Run Query to Fetch Cricket Data
cricket_team.print_response(
    "Get the latest score of the India vs Australia match, recent stats for Virat Kohli, and cricket news.", 
    stream=True
)
