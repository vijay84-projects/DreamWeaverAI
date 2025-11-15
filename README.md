🧠 1. Overview

DreamWeaver AI is a multi-agent intelligent system that converts a user’s dreams, imagination, or subconscious ideas into real, executable code.

This project was created for the Kaggle + Google AI Agents Intensive (Nov 2025) under the Freestyle Track.

The system takes any dream-like natural-language description and passes it through a pipeline of specialized agents:

Dream Interpreter Agent – extracts entities, metaphors, actions

Concept Mapper Agent – maps dream meaning → computer science concepts

Code Planner Agent – creates architecture + pseudocode

Code Generator Agent – generates the actual executable Python code

Evaluation Agent – runs the generated code + returns feedback

Logger Tool – stores every dream and output for learning

This project demonstrates multi-agent coordination, tool use, code execution, structured workflows, and Gemini LLM integration.

🎯 2. Problem Statement

People often get complex, creative ideas through dreams or imagination.
But they cannot convert those ideas into actual code.

DreamWeaver AI solves this problem by:

Understanding any dream-like description

Mapping it to CS concepts

Creating a coding plan

Generating the complete working code

Testing it

Explaining what it did

It acts as a creative-to-technical translator.

🚀 3. Core Features Used (Required by Kaggle)

This project uses more than 3 required agent concepts:

✔ Multi-Agent Architecture

Sequential agents

Orchestrator agent

Specialized agents for interpretation → mapping → planning → generation → evaluation

✔ Tools

Custom file logging tool

Code execution tool (safe simulated environment)

✔ Sessions & Memory

Structured outputs passed as dataclasses

Logs saved persistently for follow-up learning

✔ Context Engineering

System prompts for each agent

Structured reasoning responses

Decomposition of tasks

✔ Observability

Built-in result logs

Evaluation feedback after runtime

🏗️ 4. Architecture
User Dream
     │
     ▼
[1] Dream Interpreter Agent
     │
     ▼
[2] Concept Mapper Agent
     │
     ▼
[3] Code Planner Agent
     │
     ▼
[4] Code Generator Agent
     │
     ▼
[5] Evaluation Agent (execution + tests)
     │
     ▼
[6] Dream Logger Tool → saved to /dream_logs
     │
     ▼
Final Output (Code + Feedback)

📂 5. Project Structure
DreamWeaverAI/
│
├── agent.py                # Main multi-agent system
├── tools.py                # Custom tools
├── generated_code.py       # Optional generated file
├── requirements.txt        # Project dependencies
├── README.md               # This file
│
└── tests/
      └── test_eval.py      # Evaluation tests (pytest-style)

⚙️ 6. Installation
1️⃣ Clone the repo:
git clone https://github.com/vijay84-projects/DreamWeaverAI.git
cd DreamWeaverAI

2️⃣ Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install dependencies:
pip install -r requirements.txt

4️⃣ Add .env (Do NOT upload to GitHub)
GEMINI_API_KEY=your_key
GOOGLE_CLOUD_PROJECT=your_project
GOOGLE_CLOUD_REGION=us-central1

🧪 7. Running the Agent System

Run DreamWeaver:

python agent.py


Enter your dream:

I saw glowing balls racing through a maze.


Sample Output:

Generated Python code

Evaluation results

Feedback

Logs written to /dream_logs

🔍 8. Running Tests
cd tests
python test_eval.py


Expected:

🎉 All tests passed! ✔✔✔

🤖 9. Example Generated Code

The Code Generator Agent produces fully working Python code, for example:

def simulate_climb(max_steps, fail_probability):
    ...

🎬 10. Optional YouTube Video (For Bonus Points)

To get +10 bonus points, record a 2–3 min video:

Problem

Why agents

Architecture

Live demo

What you learned

Include the YouTube link in the Kaggle submission.

🏆 11. Why This Project Stands Out

Highly innovative (dream → code transformer)

Unique Freestyle category entry

Clear multi-agent architecture

Professional-quality implementation

Fully tested

Clean, modular, documented code

Practical + creative + technical

👨‍💻 12. Author

Telugu Vijay (Vijju)
B.Tech CSE
DreamWeaver AI Project – Kaggle x Google Agents Intensive (Nov 2025)

🎉 13. Final Note

This project meets all Kaggle Capstone requirements:

✔ pitch
✔ architecture
✔ multi-agent system
✔ tool use
✔ code execution
✔ evaluation
✔ documentation
✔ working code
✔ unit tests
