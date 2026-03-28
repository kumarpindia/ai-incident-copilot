import os
from openai import OpenAI
    
# Create OpenAI client (require API key)
apikey = os.getenv("OPENAI_API_KEY")
api_key_missing = False
client_init_error = None
if not apikey:
    api_key_missing = True
    client = None
else:
    # Try to create OpenAI client; if the client library causes init errors,
    # fall back to None so the app uses the REST fallback path.
    try:
        client = OpenAI(api_key=apikey)
    except Exception as e:
        client = None
        client_init_error = str(e)


def generate_diagnosis(query, contexts):
    # Placeholder for actual LLM interaction logic
    # Replace with code to generate diagnosis based on the query and retrieved contexts
    # For example, you could use an LLM API to get a response like this:
    # response = llm_api.generate_response(query, contexts)
    # return response

    context_text = "\n".join(contexts)

    prompt = f"""
You are an SRE incident assistant.

User question: 
{query}

Relevant context:
{context_text}

Provide:
1. Possible cause of the incident
2. Evidence
3. Suggested actions to resolve the incident
"""

    # Simulated response for demonstration purposes
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an SRE incident assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7,
    )
    
    return response.choices[0].message.content.strip()
