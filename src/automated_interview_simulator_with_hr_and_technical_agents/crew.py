from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.candidate_io import AskCandidateTool

@CrewBase
class AutomatedInterviewSimulatorWithHrAndTechnicalAgentsCrew():

    @agent
    def hr_interviewer(self)->Agent:
        return Agent(
            config=self.agents_config['hr_interviewer'],
        )
    @agent
    def technical_interviewer(self)->Agent:
        return Agent(
            config=self.agents_config['technical_interviewer'],
        )
    @agent
    def feedback_generator(self)->Agent:
        return Agent(
            config=self.agents_config['feedback_generator'],
        )


    @task
    def conduct_behavioral_interview(self)->Task:
        return Task(
            config=self.tasks_config['conduct_behavioral_interview'],
            tools=[AskCandidateTool()],
        )
    @task
    def conduct_technical_interview(self)->Task:
        return Task(
            config=self.tasks_config['conduct_technical_interview'],
            tools=[AskCandidateTool()],
        )
    @task
    def generate_feedback_report(self)->Task:
        return Task(
            config=self.tasks_config['generate_feedback_report'],
            tools=[],
        )
    @crew
    def crew(self) -> Crew:
        #this will create the automated interview simulator with hr and technical agents crew

        return Crew(
            agents=self.agents, #automatically created by agent decorator
            tasks=self.tasks,  #automatically created by task decorator
            process=Process.sequential,
            verbose=True,
        )
