import time
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os
import random

# Load API keys
load_dotenv()

# ✅ Function to get stock symbols
def lookup_company_symbol(company: str) -> str:
    symbols = {"Infosys": "INFY", 
               "Tesla": "TSLA", 
               "Apple": "AAPL", 
               "Microsoft": "MSFT", 
               "Amazon": "AMZN", 
               "Google": "GOOGL"}
    return symbols.get(company, "Unknown")

# ✅ Stock Data Agent
stock_agent = Agent(
    name="Stock Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Fetch stock prices, fundamentals, and analyst recommendations."],
)

# ✅ Company Lookup Agent (Previously Symbol Agent)
company_lookup_agent = Agent(
    name="Company Lookup Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[lookup_company_symbol],
    instructions=["Find stock symbols for companies based on their names."],
)

# ✅ Main Finance Team Agent (Combining Both)
finance_team = Agent(
    name="Finance Team",
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[stock_agent, company_lookup_agent],
    instructions=["Fetch stock data and company symbols together."],
)

# ✅ Function to handle API rate limits and retries
def run_with_retry(agent, query, retries=3, delay=10):
    for attempt in range(retries):
        try:
            response = agent.run(query)
            return response
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                wait_time = random.uniform(delay, delay + 5)  # Random delay between attempts
                print(f"Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries reached. Could not complete the request.")
                return None

# ✅ Run Query with retry handling
response = run_with_retry(finance_team, "Compare stock data for Apple and Google.")
if response:
    print(response)
else:
    print("Failed to get a response after retries.")
