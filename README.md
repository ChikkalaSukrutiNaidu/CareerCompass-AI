# 🎯 CareerCompass AI

> An Intelligent Multi-Agent AI Decision Support System for Placement Offer Evaluation

CareerCompass AI is an AI-powered decision support system that helps students compare multiple placement offers and choose the one that best aligns with their career goals and personal preferences.

Unlike traditional recommendation systems, CareerCompass uses multiple specialized AI agents that collaborate through LangGraph. Each agent performs a dedicated task, and an Explainable Scoring Engine combines their outputs to generate transparent, personalized recommendations.

---

# 🚀 Problem Statement

Students often receive multiple placement offers but struggle to determine which opportunity best supports their long-term career aspirations.

The decision usually depends on multiple factors such as:

- Career Goals
- Technology Exposure
- Career Growth
- Salary
- Learning Opportunities
- Preferred Location
- Work Style
- Higher Studies Plans

CareerCompass AI automates this decision-making process using multiple AI agents and explainable reasoning.

---

# ✨ Key Features

- 🤖 Multi-Agent AI Architecture using LangGraph
- 🎯 Goal Analysis Agent
- 💼 Offer Intelligence Agent
- 📍 Preference Matching Agent
- ⚙️ Explainable Scoring Engine
- 📊 AI-Powered Recommendation Report
- 🔄 Shared State Management using Pydantic
- 🧠 Structured LLM Outputs
- 📈 Transparent Decision Making

---

# 🏗️ System Architecture

```text
                    User
                      │
                      ▼
               LangGraph Workflow
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Goal Agent   Offer Agent   Preference Agent
        │             │             │
        └─────────────┼─────────────┘
                      ▼
          Explainable Scoring Engine
                      ▼
          Recommendation Agent
                      ▼
             Final Recommendation
```

---

# 🤖 AI Agents

## 🎯 Goal Agent

Analyzes the student's profile and identifies career priorities.

### Inputs

- Career Goal
- Higher Studies Preference
- Preferred Work Style

### Outputs

- Technology Priority
- Career Growth Priority
- Salary Priority
- Work-Life Balance Priority
- Higher Studies Priority

---

## 💼 Offer Intelligence Agent

Analyzes each placement offer independently.

### Evaluates

- Technology Exposure
- Career Growth
- Salary Potential
- Learning Opportunities
- Brand Value

---

## 📍 Preference Agent

Measures how well each placement offer aligns with the student's personal preferences.

### Evaluates

- Preferred Location
- Work Style Compatibility
- Higher Studies Support

---

## ⚙️ Explainable Scoring Engine

Instead of allowing the LLM to make the final decision, CareerCompass calculates weighted scores using Python.

This makes every recommendation transparent and explainable.

Example:

Technology Score

```
Technology Rating × Technology Priority
```

Career Growth Score

```
Growth Rating × Growth Priority
```

Overall Score

```
Technology
+ Career Growth
+ Salary
+ Location
+ Work Style
+ Higher Studies
```

---

## 🧠 Recommendation Agent

The Recommendation Agent does not perform additional reasoning.

Instead, it converts the scoring results into a professional recommendation report including:

- Recommended Company
- Final Score
- Strengths
- Trade-offs
- Runner-Up Offer
- Detailed Explanation

---

# ⚙️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Backend Development |
| LangGraph | Multi-Agent Workflow |
| LangChain | LLM Integration |
| Groq API | Large Language Model |
| Pydantic | Structured Data Models |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
CareerCompass/
│
├── app/
│   │
│   ├── agents/
│   │     ├── goal_agent.py
│   │     ├── offer_agent.py
│   │     ├── preference_agent.py
│   │     └── recommendation_agent.py
│   │
│   ├── graph/
│   │     └── builder.py
│   │
│   ├── models/
│   │
│   ├── prompts/
│   │
│   ├── scoring/
│   │     └── score_engine.py
│   │
│   └── services/
│
├── test_graph.py
├── test_score_engine.py
├── test_recommendation.py
├── requirements.txt
└── README.md
```

---

# 🔄 Workflow

```text
Student Profile
        │
        ▼
Goal Agent
        │
        ▼
Offer Intelligence Agent
        │
        ▼
Preference Agent
        │
        ▼
Explainable Scoring Engine
        │
        ▼
Recommendation Agent
        │
        ▼
Final Recommendation Report
```

---

# 📊 Current Development Status

### ✅ Completed

- Project Setup
- GitHub Repository
- LangGraph Integration
- Shared State Management
- Goal Agent
- Offer Intelligence Agent
- Preference Agent
- Explainable Scoring Engine
- Recommendation Agent
- End-to-End LangGraph Workflow

---

### 🚧 Upcoming

- FastAPI Backend
- REST APIs
- React Frontend
- Interactive Dashboard
- Docker Support
- Deployment
- Documentation
- Unit Testing

---

# 🎯 Future Enhancements

- Dynamic Weight Adjustment
- Scenario-Based Career Analysis
- Offer Letter Parsing Agent
- Company Research Agent
- Resume-Based Recommendation
- Authentication & User Profiles
- Analytics Dashboard

---

# ▶️ Getting Started

## Clone Repository

```bash
git clone https://github.com/<your-username>/CareerCompass.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python test_recommendation.py
```

---

# 📌 Current Version

**Version:** v0.1.0

Status:

🚧 Under Active Development

---

# 👩‍💻 Author

**Sukruti Naidu Chikkala**

B.Tech – Information Technology

Shri Vishnu Engineering College for Women

---

## ⭐ Project Vision

CareerCompass AI aims to evolve into a complete AI-powered career decision support platform where multiple specialized AI agents collaborate to provide transparent, personalized, and explainable placement recommendations for students.