Overview
This project was built as part of my IIT Jammu internship (Techible + I3C Jammu) to explore multi-agent AI workflows using CrewAI.

The simulator mimics a real interview process:

HR Agent → asks behavioral questions and rates responses

Technical Agent → asks role-specific technical questions and rates responses

Feedback Agent → combines ratings and generates a structured feedback report (Markdown)

Features
Simulates HR + Technical rounds for any chosen role

Asks questions one-by-one and waits for user answers

Scores each answer (1–10) with brief reasoning

Generates Markdown feedback with:

Strengths and weaknesses

Overall readiness score

Actionable tips for improvement

Easy to extend (resume parsing, PDF export, Discord bot integration)

Tech Stack
CrewAI – Multi-agent orchestration framework

OpenAI API – LLM for question generation & scoring

Python 3.9+

Project Structure
bash
Copy
Edit
automated_interview_simulator_with_hr_and_technical_agents/
│
├── crew.py               # Defines agents and tasks
├── main.py               # Entry point to run the simulator
├── config/               # Task/agent configuration files
├── tools/                # (Optional) Custom tools folder
├── requirements.txt      # Python dependencies
└── .env.example          # Environment variable template
Setup & Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/<your-username>/automated-interview-simulator.git
cd automated-interview-simulator/src/automated_interview_simulator_with_hr_and_technical_agents
2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
Usage
Run the simulator:

bash
Copy
Edit
python main.py
Example Flow:

Enter the role you want to simulate (e.g., Backend Engineer).

Answer behavioral questions one by one.

Answer technical questions one by one.

Get a Markdown feedback report summarizing your performance.

Future Improvements
Add resume parsing to tailor questions automatically

Export feedback to PDF

Turn into a Discord/Slack bot for mock interview practice

Role-specific difficulty scaling (junior → senior)
