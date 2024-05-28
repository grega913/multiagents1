from crewai import Agent
from langchain_groq import ChatGroq
import os
from crewai_tools import SerperDevTool

groq_api_key = os.environ.get('GROQ_API_KEY')
serper_api_key = os.environ.get('SERPER_API_KEY')

#os.environ["SERPER_API_KEY"] = 'a13f459d75dd2f4e7793f28fa9d41d7ff1a59e86'


search_tool = SerperDevTool()

llm = ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key=groq_api_key)


''' AGENTS'''

researcher = Agent(
    llm=llm,
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
    "Driven by curiosity, you're at the forefront of"
    "innovation, eager to explore and share knowledge that could change"
    "the world."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Creating a writer agent with custom tools and delegation capability
writer = Agent(
    llm=llm,
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
    ),
    tools=[search_tool],
    allow_delegation=False
)


