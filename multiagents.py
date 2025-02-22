from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo  # For fetching news
from phi.tools.coingecko import CoinGecko  # For fetching cryptocurrency prices
from phi.tools.amazon import AmazonSearch  # For searching e-commerce products
from phi.tools.skyscanner import SkyscannerFlightSearch, SkyscannerHotelSearch  # For fetching flights and hotels
from phi.tools.sports import SportsNews  # For fetching sports news
from dotenv import load_dotenv

# Load environment variables (e.g., API keys)
load_dotenv()

# ✅ Unified Groq Model
groq_model = Groq(id="llama-3.3-70b-versatile")  # AI model for processing data

# ✅ News Agent (Fetches latest financial news)
news_agent = Agent(
    name="News Agent",
    model=groq_model,
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

# ✅ Crypto Price Agent (Fetches real-time cryptocurrency prices)
crypto_price_agent = Agent(
    name="Crypto Price Agent",
    model=groq_model,
    tools=[CoinGecko()],  # Uses CoinGecko API to fetch crypto data
    instructions=[
        "Fetch the latest price for the given cryptocurrency.",
        "Provide insights on any recent trends or price changes.",
        "Provide predictions for the next 24 hours based on market movements."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ E-commerce Product Finder Agent (Finds product reviews and prices)
ecommerce_agent = Agent(
    name="E-commerce Product Finder Agent",
    model=groq_model,
    tools=[AmazonSearch()],  # Uses AmazonSearch to find products
    instructions=[
        "Search for the latest reviews and prices of the given product.",
        "Provide comparisons of product features, prices, and user ratings.",
        "Highlight any promotions or discounts available."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Travel Agent (Fetches flight and hotel details)
travel_agent = Agent(
    name="Travel Agent",
    model=groq_model,
    tools=[SkyscannerFlightSearch(), SkyscannerHotelSearch()],  # Uses Skyscanner for flights and hotels
    instructions=[
        "Find available flights and hotels for the given destination and dates.",
        "Provide price comparisons for flights and hotels.",
        "Suggest travel tips or recommendations for the destination."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Sports News Agent (Fetches the latest sports news)
sports_news_agent = Agent(
    name="Sports News Agent",
    model=groq_model,
    tools=[SportsNews()],  # Uses SportsNews to get the latest headlines
    instructions=[
        "Search for the latest news in the world of sports.",
        "Summarize the top sports headlines and provide insights on major games or events.",
        "Include stats, player performances, and other key updates."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# ✅ Run Queries

# Financial News Query
news_agent.print_response(
    "Find and summarize the latest financial news about Tesla and NVIDIA.", 
    stream=True
)

# Crypto Price Query
crypto_price_agent.print_response(
    "Fetch the latest price for Bitcoin.", 
    stream=True
)

# Product Finder Query
ecommerce_agent.print_response(
    "Search for the latest reviews and prices of the iPhone 15.", 
    stream=True
)

# Travel Details Query
travel_agent.print_response(
    "Find flights and hotels for a trip to Paris next month.", 
    stream=True
)

# Sports News Query
sports_news_agent.print_response(
    "Find the latest sports news about the NBA.", 
    stream=True
)
