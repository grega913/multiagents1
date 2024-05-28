from crewai import  Crew
from crewai_agents import planner, writer, editor
from crewai_tasks import plan, write, edit

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=1,
)

result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})

print(result)

