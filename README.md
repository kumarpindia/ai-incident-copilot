# AI Incident Copilot

An AI-powered assistant that helps engineers diagnose and resolve production incidents by analyzing logs, incident reports, and runbooks using a Retrieval-Augmented Generation (RAG) architecture.

---

## Overview

Modern production systems generate large volumes of operational data—logs, alerts, and incident reports. During incidents, engineers must quickly sift through this information to identify root causes and take corrective action.

This project demonstrates how AI can augment incident response by:

* Retrieving relevant operational context from historical data
* Synthesizing insights using a Large Language Model (LLM)
* Providing structured, actionable troubleshooting guidance

The system acts as a **copilot for on-call engineers**, reducing time-to-diagnosis and improving operational efficiency.

---

## Key Capabilities

* Natural language querying of incidents and logs
* Context-aware retrieval across multiple data sources
* Root cause hypothesis generation
* Evidence-backed reasoning
* Suggested remediation steps

---

## System Architecture

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline tailored for operational use cases.

### High-Level Flow

```
User Query
    ↓
Streamlit UI
    ↓
Retriever (Chroma Vector DB)
    ↓
Relevant Context (logs, incidents, runbooks)
    ↓
LLM (OpenAI)
    ↓
Structured Diagnosis
```

### Data Flow

1. **Ingestion**

   * Load logs, incident reports, and runbooks
   * Chunk documents
   * Generate embeddings
   * Store in Chroma vector database

2. **Retrieval**

   * Convert user query into embedding
   * Perform similarity search
   * Retrieve top-k relevant context

3. **Reasoning**

   * Combine query + retrieved context
   * Generate diagnosis using LLM

4. **Presentation**

   * Display diagnosis and supporting evidence via UI

---

## Tech Stack

* **Language:** Python
* **LLM:** OpenAI API
* **Embeddings:** OpenAI Embeddings
* **Vector Store:** ChromaDB
* **Framework:** LangChain
* **UI:** Streamlit

---

## Project Structure

```
app/
  __init__.py
  ui.py              # Streamlit UI
  ingestion.py       # Data ingestion & vector DB creation
  retriever.py       # Context retrieval logic
  llm_agent.py       # LLM prompt orchestration

evaluation/
  dataset.json       # Evaluation dataset
  evaluate.py        # Evaluation runner
  evaluator.py       # LLM-based scoring

data/
  incidents/         # Incident reports
  logs/              # Application logs
  runbooks/          # Troubleshooting guides

chroma_db/           # Persisted vector database
```

---

## Getting Started

### 1. Setup Environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set API Key

```bash
export OPENAI_API_KEY=your_key_here
```

---

### 4. Build Vector Database

```bash
python -m app.ingestion
```

---

### 5. Run Application

```bash
streamlit run app/ui.py
```

---

## Example Queries

* "Why is the payment service failing?"
* "Have we seen database timeout errors before?"
* "What should I check for high API latency?"

---

## Example Output

```
Possible Root Cause:
Database connection pool exhaustion

Evidence:
Similar incident INC-2025-102 with identical timeout patterns

Suggested Actions:
- Check DB connection pool metrics
- Restart affected service
- Increase pool size if saturation observed
```

---
## Evaluation Framework

This project includes a lightweight evaluation framework to assess the quality and reliability of the AI system.

Unlike typical demo applications, this system is evaluated across multiple dimensions to ensure that responses are correct, grounded, and useful.

---

## Why Evaluation Matters

LLM-based systems can produce fluent but incorrect or ungrounded responses. To move beyond demo-quality implementations, it is essential to introduce systematic evaluation.

This project incorporates evaluation to:

Measure answer correctness and completeness
Detect potential hallucinations
Validate retrieval effectiveness
Enable iterative improvement of the system

---

## Evaluation Approach

The evaluation framework follows a dataset-driven methodology:

A set of predefined questions with expected answers is created
The system generates responses using the full RAG pipeline
An LLM-based evaluator scores the responses
Aggregate metrics are computed

---

## Running Evaluation
```bash
python -m evaluation.evaluate
```

---

## Example Evaluation Output
```bash
Question: Why is payment service failing?
Expected: database connection pool exhaustion

Actual: The issue is likely caused by database connection saturation...

Score: 4/5
Reason: Correct root cause identified but lacks detailed remediation steps.

------------------------------
Average Score: 4.2/5
```
---

## Evaluation Dimensions
* **Correctness** — Does the answer match the expected outcome?
* **Completeness** — Does it cover all relevant aspects?
* **Grounding** — Is the answer supported by retrieved context?
* **Clarity** — Is the explanation actionable and understandable?


## Evaluation Limitations
* Dataset is small and synthetic
* LLM-based scoring introduces some subjectivity
* Retrieval-specific metrics (precision/recall) not yet implemented

---

## Design Considerations

This project intentionally focuses on **real-world engineering workflows**, not just chatbot functionality.

### Key Decisions

* **RAG over fine-tuning**
  Enables grounding in operational data without retraining models

* **Separation of concerns**
  UI, retrieval, and reasoning layers are decoupled

* **Local vector store (Chroma)**
  Simplifies setup while enabling fast similarity search

* **Explainability-first design**
  Retrieved evidence can be surfaced alongside answers

---

## Limitations

* Uses synthetic / sample data (not real production telemetry)
* Retrieval quality depends on chunking and data quality
* No automated retrieval metrics yet

---

## Future Improvements

* Add retrieval metrics (precision@k, recall@k)
* Implement hallucination detection
* Integrate real observability systems (Prometheus, ELK)
* Add multi-agent workflow (retrieval + reasoning + validation)
* Expand evaluation dataset

---

## Author

Built as part of a transition into AI/ML systems, focusing on **AI applications for engineering productivity and reliability**.

---

## Key Takeaway

This project demonstrates how AI can be applied to **real operational problems**, combining:

* LLM capabilities
* Retrieval systems
* Software architecture
* Evaluation and quality measurement

---
