import json
from dotenv import load_dotenv, find_dotenv

# Load environment variables (ensure the .env next to this file is used even if cwd differs)
dotenv_path = find_dotenv(usecwd=True)
if dotenv_path:
    load_dotenv(dotenv_path)

from app.retriever import get_relevant_context
from app.llm_agent import generate_diagnosis
from evaluation.evaluator import evaluate_answer

def run_evaluation():

    with open("evaluation/dataset.json") as f:
        dataset = json.load(f)

    scores = []

    for case in dataset:

        question = case["question"]
        expected = case["expected_answer"]

        # Run pipeline to get actual answer
        contexts = get_relevant_context(question)
        actual = generate_diagnosis(question, contexts)

        # Evaluate the answer
        score, reason = evaluate_answer(question, expected, actual)
        scores.append(score)

        print("\n==============================")
        print("Question:", question)
        print("Expected:", expected)
        print("Actual:", actual)
        print("Score:", score/5)
        print("Reason:", reason)
        print("-" * 50)

    avg_score = sum(scores) / len(scores) if scores else 0

    print("\n==============================")
    print(f"\nAverage Score: {avg_score:.2f}/5")


if __name__ == "__main__":
    run_evaluation()