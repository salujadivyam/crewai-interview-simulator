from crewai.tools import BaseTool
from pydantic import BaseModel, Field
class AskCandidateInput(BaseModel):
    question: str = Field(..., description="The interview question to ask the candidate")
    
class AskCandidateTool(BaseTool):
    name: str = "ask_candidate"
    description: str = (
        "Ask the candidate a single interview question and wait for their typed answer. "
        "Use this for every question you want to ask — do not invent the candidate's answer."
    )
    args_schema: type[BaseModel] = AskCandidateInput

    def _run(self, question: str) -> str:
        print(f"\n{question}")
        answer = input("Your answer: ")
        return answer