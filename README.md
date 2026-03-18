# 🤖 AI-Powered Research Paper Analyzer (Multi-Agent System)

## 📌 Overview

This project is a **multi-agent AI system** that automatically reads, analyzes, and summarizes academic research papers.

It uses **LangGraph + LangChain** to orchestrate multiple specialized AI agents that collaborate like a research team to generate a structured **research brief**.

---

## 🎯 Problem Statement

Reading and understanding research papers is time-consuming and requires extracting key information such as:

* Methodology
* Findings
* Citations
* Key insights

This system automates the process using **AI agents with quality control and iteration logic**.

---

## 🧠 Architecture

The system follows a **multi-agent orchestration design**:

```
Input (PDF/Text)
        ↓
🧑‍💼 Boss Agent (Orchestrator)
        ↓
🔍 Paper Analyzer Agent
        ↓
🧪 Review Agent (Quality Check)
        ↓ (if approved)
📝 Summary Agent → Review → Retry if needed
📚 Citation Agent → Review → Retry if needed
💡 Insights Agent → Review → Retry if needed
        ↓
🧑‍💼 Boss Agent (Combines Results)
        ↓
📄 Final Research Brief
```

---

## 🤖 Agents Description

### 🧑‍💼 Boss Agent

* Controls the workflow
* Delegates tasks to sub-agents
* Combines final outputs

### 🔍 Paper Analyzer Agent

* Extracts:

  * Problem statement
  * Methodology
  * Key findings

### 📝 Summary Agent

* Generates a **150–200 word executive summary**

### 📚 Citation Extractor Agent

* Extracts and organizes references from the paper

### 💡 Insights Agent (Bonus)

* Generates actionable insights and takeaways

### 🧪 Review Agent (Critical Component)

* Evaluates each output
* Assigns score (1–10)
* Provides feedback
* Triggers retry if score < 7
* Limits retries to 2 (prevents infinite loops)

---

## 🔁 Iteration Logic

The system ensures quality using automated feedback loops:

```
If review_score < 7:
    Retry agent (max 2 times)
Else:
    Approve and proceed
```

---

## ⚙️ Tech Stack

* **LangGraph** – Multi-agent workflow orchestration
* **LangChain** – LLM abstraction
* **OpenAI (GPT-4o-mini)** – Language model
* **Python** – Backend
* **pdfplumber** – PDF text extraction
* **dotenv** – Environment variable management

---

## 📂 Project Structure

```
ai-research-analyzer/
│
├── agents/
│   ├── analyzer.py
│   ├── summary.py
│   ├── citation.py
│   ├── insights.py
│   ├── reviewer.py
│
├── utils/
│   ├── pdf_loader.py
│   └── llm.py
│
├── graph.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd ai-research-analyzer
```

---

### 2️⃣ Create Virtual Environment

```
python3.11 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
pip install langchain-openai
```

---

### 4️⃣ Add API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the Project

```
python main.py
```

---

## 📥 Input

* Research paper PDF (local file)

---

## 📤 Output

A structured **Research Brief** containing:

* 🔍 Analysis (problem, methodology, findings)
* 📝 Executive Summary (150–200 words)
* 📚 Citations & References
* 💡 Key Insights

---

## 🧪 Sample Output

```
📌 FINAL RESEARCH BRIEF

🔍 Analysis:
...

📝 Summary:
...

📚 Citations:
...

💡 Insights:
...
```

---

## 🎥 Demo Video

👉 [Add Google Drive Link Here]

---

## 🌟 Key Features

* ✅ Multi-agent architecture (Boss + Sub-agents + Review Agent)
* ✅ Automated quality control with retry logic
* ✅ Structured output generation
* ✅ PDF processing support
* ✅ Modular and scalable design

---

## ⚠️ Limitations

* Large PDFs may require chunking (context limit)
* Citation extraction may include noise (can be improved with parsing)
* Requires API key (OpenAI)

---

## 📌 Future Improvements

* Add Streamlit/React UI
* Implement RAG for long papers
* Improve citation extraction using regex/NER
* Add support for paper URLs

---

## 👨‍💻 Author

**Sohit Kumar**

---

## 📜 License

This project is for educational and evaluation purposes.
