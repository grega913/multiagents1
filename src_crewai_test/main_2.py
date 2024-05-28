from crewai import  Crew
from crewai_agents_2 import researcher, writer
from crewai_tasks_2 import research_task, write_task

crew2 = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=2,
)

result2 = crew2.kickoff(inputs={"topic": "Artificial Intelligence"})

print(result2)