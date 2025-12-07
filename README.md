# multi-agent-social-engine-
A multi-agent AI system where LLM-powered personas interact autonomously using unique personality profiles. Includes turn-based dialogue, basic tool use, and an extensible architecture for memory, matching, and future AI social simulations.
# Multi-Agent AI Social Interaction Engine
### Final Project for [AIM-5000-1]

This project implements a **Multi-Agent Social Engine** where two or more AI personas autonomously interact based on their personality profiles and communication styles. The system generates persona traits from publicly available MBTI datasets and orchestrates multi-turn conversations between AI agents. 

Agents can use external tools (e.g., web search or sentiment analysis) to enrich their reasoning and exhibit emergent behaviors such as cooperation, conflict, or emotional bonding.

The architecture is intentionally designed to support future extensions:
- **Memory Module (RAG)**
- **Semantic Matching Engine (compatibility scoring)**
- **Multi-agent social graph simulation**

---

## 🔧 Features (MVP version)
- Persona generation from MBTI dataset (Kaggle)
- Two LLM-powered agents with unique identities
- Turn-based multi-agent conversation orchestrator
- Tool use: sentiment analysis of each message
- Streamlit UI for interactive demo

---

## 📊 Public Dataset
This project uses the MBTI-500 personality dataset from Kaggle:  
https://www.kaggle.com/datasets/datasnaek/mbti-type

---

## 🏗️ Project Structuremulti-agent-social-engine/
│
├── agents/
│ ├── agent.py # Defines Agent class
│ ├── persona_builder.py # Builds persona from MBTI dataset
│
├── orchestrator/
│ ├── dialogue_manager.py # Controls agent turn-taking dialogue
│
├── tools/
│ ├── sentiment_tool.py # Sentiment analysis module
│
├── ui/
│ ├── app.py # Streamlit demo interface
│
├── data/
│ ├── mbti_sample.csv # Sample MBTI dataset
│
├── main.py # Terminal version
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## 🧪 Sample Architecture Diagram


            ┌──────────────────────┐
            │  Persona Builder     │
            │  (MBTI dataset)      │
            └──────────┬───────────┘
                       ▼
               ┌────────────────┐
               │   Agent A      │
               └───────┬────────┘
                       ▼
                ┌───────────────┐
                │ Dialogue       │
                │ Orchestrator   │
                └───────┬────────┘
                       ▼
               ┌────────────────┐
               │   Agent B      │
               └───────────────┘
                       ▼
          ┌────────────────────────────┐
          │    Tool Layer (Sentiment)   │
          └────────────────────────────┘


---

## ▶️ Running the Project

### 1. Install Dependencies


pip install -r requirements.txt


### 2. Run Streamlit UI


streamlit run ui/app.py


### 3. Or run from terminal


python main.py


---

## 📊 Dataset Used

MBTI Personality Dataset (Kaggle)  
https://www.kaggle.com/datasets/datasnaek/mbti-type  

Data is used to generate persona traits and language patterns for each agent.

---

## 🧠 Future Extensions

- **Long-term memory** with RAG (FAISS + LLM)  
- **Semantic compatibility scoring** between agents  
- **Emotional state tracking**  
- **Multi-agent social world simulation**  
- **Emergent behavior logging**  
- **Tool-using agents** (search, reasoning, actions)  

---

## 👤 Author  
**Alex Ji**  
Yeshiva University — Computer Science (AI Track)  
Fall 2024 Final Project  
