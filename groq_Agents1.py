import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

# Load API keys
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")  # Ensure API key is set in your .env

# 🎯 Function to get stock symbols
def get_company_symbol(company: str) -> str:
    """Convert company name to stock symbol."""
    symbols = {
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")

# 🎯 Stock Data Agent
stock_agent = Agent(
    name="Stock Data Agent",
    model=Groq(id="llama-3.3-70b-versatile", api_key=groq_api_key),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use tables to display stock data."],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# 🎯 Main Finance Analysis Team
agent_team = Agent(
    name="Finance Analysis Team",
    model=Groq(id="llama-3.3-70b-versatile", api_key=groq_api_key),
    team=[stock_agent],
    instructions=["Use tables for comparisons and include analyst insights."],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# 🎯 Streamlit UI
st.set_page_config(page_title="📈 Financial Insights", layout="wide")
st.title("📈 Financial AI - Stock Prices, Analyst Ratings & Fundamentals")

# User Input
col1, col2 = st.columns(2)
with col1:
    company_1 = st.text_input("Enter first company (e.g., 'Tesla', 'Microsoft'):")
with col2:
    company_2 = st.text_input("Enter second company (optional):")

if st.button("Get Stock Analysis"):
    if company_1:
        symbol_1 = get_company_symbol(company_1)
        symbol_2 = get_company_symbol(company_2) if company_2 else None

        if symbol_1 != "Unknown":
            with st.spinner(f"Fetching financial data for {company_1} ({symbol_1})..."):
                query = f"Summarize and compare analyst recommendations and fundamentals for {symbol_1}"
                if symbol_2 and symbol_2 != "Unknown":
                    query += f" and {symbol_2}"
                query += ". Show in tables."

                response = agent_team.run(query)  # ✅ FIXED: Using `.run()`
                st.markdown(response)  # ✅ Display result properly
        else:
            st.warning(f"Company '{company_1}' not found. Please try another.")

# Run using: `streamlit run app.py`
