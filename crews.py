from crewai import Crew, Process
from tasks import create_tasks
import os
# os.environ["OPENAI_API_KEY"] = "sk-mksuGXjm2woDgfZOOqRpZHUsBF4lauqVOn2AES81AuT3BlbkFJFA5H_2s_ax_R9aGLuuUwnaLmlT5JtVFkuRJjNl9mYA"
def create_crews(topic):
    # Create tasks dynamically based on the topic
    software_task, researcher_task, news_task = create_tasks(topic)

    # Crew 1: Researcher and Analyst
    crew1 = Crew(
        agents=[software_task.agent],
        tasks=[software_task],
        verbose=False,
        memory=False,
        max_rpm=10,
        
    )

    # Crew 2: Internet Explorer
    crew2 = Crew(
        agents=[news_task.agent],
        tasks=[news_task],
        verbose=False,
        memory=False,
        max_rpm=10,
        
    )
    
    crew3 = Crew(
        agents=[researcher_task.agent],
        tasks=[researcher_task],
        verbose=False,
        memory=False,
        max_rpm=10,
        
    )
    return crew1, crew2, crew3
