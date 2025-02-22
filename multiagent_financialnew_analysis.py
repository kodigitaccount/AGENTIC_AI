import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo  # Fetches news
from dotenv import load_dotenv

# Load environment variables (e.g., API keys)
load_dotenv()

# ✅ News Agent: Fetches latest financial news
news_agent = Agent(
    name="News Agent",
    model=Groq(id="llama-3.3-70b-versatile"),  # Ensure valid model ID
    tools=[DuckDuckGo()],  # Uses DuckDuckGo for fetching news
    instructions=[
        "Search for the latest financial news about the given company.",
        "Summarize the top news articles.",
        "Provide key insights in markdown format."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Market Analysis Agent: Analyzes stock trends
market_analysis_agent = Agent(
    name="Market Analysis Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Analyze recent stock trends based on financial news data.",
        "Identify key stock movements and patterns.",
        "Provide insights on market fluctuations."
    ],
    markdown=True,
    debug_mode=True,
)

# ✅ Sentiment Analysis Agent: Analyzes sentiment of financial news
sentiment_analysis_agent = Agent(
    name="Sentiment Analysis Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Perform sentiment analysis on the latest financial news.",
        "Determine whether the sentiment is positive, negative, or neutral.",
        "Provide a brief sentiment summary."
    ],
    markdown=True,
    debug_mode=True,
)

# ✅ Fetch News & Perform Analysis
try:
    print("\n🔹 Fetching Financial News...")
    news_agent.print_response("Find and summarize the latest financial news about Tesla and NVIDIA.", stream=True)

    print("\n🔹 Performing Market Analysis...")
    market_analysis_agent.print_response("Analyze stock trends based on the news provided above.", stream=True)

    print("\n🔹 Performing Sentiment Analysis...")
    sentiment_analysis_agent.print_response("Analyze sentiment of the news provided above.", stream=True)

except Exception as e:
    print(f"❌ Error: {e}")
