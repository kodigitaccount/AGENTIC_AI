import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.tools import DuckDuckGoSearchRun
from langchain.llms import Ollama
from langchain.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory

# ✅ Load Open-Source LLM via Ollama
llm = ChatOllama(model="mistral")  # or "llama3"

# ✅ Tools (Web Search)
search_tool = DuckDuckGoSearchRun()

# ✅ Stock Market News Agent
news_agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=ConversationBufferMemory(),
    verbose=True,
)

# ✅ Company Insights Agent
company_agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=ConversationBufferMemory(),
    verbose=True,
)

# ✅ Market Trend Analysis Agent
trend_agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=ConversationBufferMemory(),
    verbose=True,
)

# ✅ Streamlit UI
st.title("📊 Multi-Agent Financial Analysis (Open-Source LLM)")

company = st.text_input("Enter a company name (e.g., Tesla, Microsoft):")

if st.button("Get Insights"):
    if company:
        st.write("🔍 Fetching latest stock market news...")
        news_response = news_agent.run(f"Find latest financial news about {company}")

        st.write("🏢 Fetching company insights...")
        company_response = company_agent.run(f"Provide key insights about {company}, like CEO, industry, and revenue.")

        st.write("📈 Analyzing stock market trends...")
        trend_response = trend_agent.run("Summarize key stock market trends affecting major companies.")

        # Display results
        st.subheader("📰 Latest Stock Market News")
        st.markdown(news_response)

        st.subheader(f"🏢 Insights on {company}")
        st.markdown(company_response)

        st.subheader("📈 Market Trend Analysis")
        st.markdown(trend_response)

    else:
        st.warning("Please enter a company name.")

