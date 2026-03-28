import streamlit as st
from retriever import get_relevant_context
from llm_agent import generate_diagnosis
#from app.retriever import get_relevant_context
#from app.llm_agent import generate_diagnosis


st.set_page_config(page_title="AI Incident Copilot", layout="wide")

st.title("AI Incident Copilot")

# Input section
st.subheader("Ask about your Incident")
user_query = st.text_input("Ask about your Incident")

if st.button("Ask"):
    if user_query:
        # Placeholder for API call or processing logic
        # Replace with actual function that returns possible_cause, evidence, suggestions
        #possible_cause = "Loading..."
        #evidence = "Loading..."
        #suggestion_actions = "Loading..."
        
        contexts = get_relevant_context(user_query)
        
        diagnosis = generate_diagnosis(user_query, contexts)

        # Display results
        st.write("### Analysis Results")
        st.write(diagnosis)
        #st.write(f"**Possible cause:** {possible_cause}")
        #st.write(f"**Evidence:** {evidence}")
        #st.write(f"**Suggestion actions:** {suggestion_actions}")
    else:
        st.warning("Please enter a query before submitting.")