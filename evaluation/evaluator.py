import os
from openai import OpenAI

#client = OpenAI()

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


def evaluate_answer(question, expected, actual):

    prompt = f"""
You are evaluating an AI system's answer.

Question:
{question}

Expected Answer:
{expected}

Actual Answer:
{actual}

Score the answer from 1 to 5 based on correctness and completeness.

Respond strictly in this format:
Score: <number>
Reason: <short explanation>
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    # Simple parsing
    score = int(content.split("Score:")[1].split("\n")[0].strip())
    reason = content.split("Reason:")[1].strip()

    return score, reason