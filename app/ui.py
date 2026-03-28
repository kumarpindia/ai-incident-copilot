import streamlit as st
from dotenv import load_dotenv, find_dotenv

# Load environment variables (ensure the .env next to this file is used even if cwd differs)
dotenv_path = find_dotenv(usecwd=True)
if dotenv_path:
    load_dotenv(dotenv_path)

from retriever import get_relevant_context
from llm_agent import generate_diagnosis

st.set_page_config(page_title="AI Incident Copilot", layout="wide")

st.title("AI Incident Copilot")

# Input section
st.subheader("Ask about your Incident")
with st.form(key="query_form"):
    user_query = st.text_input("", placeholder="Enter your query about the incident here...")
    ask = st.form_submit_button("Ask")

if ask:
    if user_query:
        contexts = get_relevant_context(user_query)
        diagnosis = generate_diagnosis(user_query, contexts)

        # Display results
        st.write("### Analysis Results")
        st.write(diagnosis)
    else:
        st.warning("Please enter a query before submitting.")