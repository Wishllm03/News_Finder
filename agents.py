from crewai import LLM
from tools import  tool2
from crewai import Agent
from itertools import cycle
import os
# from llm_config import LocalHuggingFaceLLM
# os.environ["OPENAI_API_KEY"] = "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"


API_KEYS = [
     "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"
]
# os.environ["OPENAI_API_KEY"] = "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"
# Create a cycle iterator for API keys
api_key_cycle = cycle(API_KEYS)

def get_next_api_key():
    return next(api_key_cycle)

# Set initial API key
os.environ["OPENAI_API_KEY"] = get_next_api_key()

# You can call get_next_api_key() whenever you hit a rate limit error
# Example usage in a try-except block:
try:
    # Your API call here
    print(f"Current API key: {os.environ['OPENAI_API_KEY']}")
    pass
except Exception as e:
    if "rate limit" in str(e).lower():
        os.environ["OPENAI_API_KEY"] = get_next_api_key()




# llm = LocalHuggingFaceLLM(model_path="C:/Users/master/Desktop/Agents/models", device = 0)
# os.environ["HUGGINGFACE_API_KEY"] = "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"
llm = LLM(
    model="openai/gpt-4o-mini"
)
llm2 = LLM(
    model = "ollama/phi4:14b-q8_0"  ,
    base_url="http://localhost:11434"
)
# llm = LLM(
#     model = "huggingface/phi3" ,
#     base_url= "http://localhost:8502" ,
#     provider="huggingface" 
# )


def create_software_agent(topic):
    return Agent(
        role='Software_Developer',
        goal=f'You are a Software Developer working for assisting software applications, You have to give solution and python code for the {topic}.',
        verbose=True,
        memory=False,
        cache=False,
        backstory=""" You are a software expert to assist in the software application development.You will give your answer based on your Pyhton expertise.
        You are a Software Developer assigned to a military technology unit, tasked with developing mission-critical applications and systems that enhance operational capabilities. 
        Your work involves designing secure, scalable, and highly reliable software for a variety of military functions, including command and control, logistics management, intelligence analysis, and battlefield communications. 
        The software must support real-time data processing and integration with both existing military hardware (such as GPS, drones, and communication systems) and software platforms.

        Consider the following requirements and challenges in your development process:

        Security: Ensure all applications meet military-grade security standards, including encryption for sensitive data, secure communication protocols, and protection against cyber threats. Implement role-based access control and audit logs for all system activities.
        Scalability and Reliability: Design the software to handle large-scale data processing and high-availability needs. The system should function effectively under both stable and low-bandwidth, high-latency environments, and remain operational in the event of network disruptions.
        Real-time Processing: Implement real-time data handling capabilities, especially in areas such as battlefield communications, sensor data processing, and live mission updates. Ensure that the system can process and respond to critical information swiftly.
        User Experience: Design intuitive and user-friendly interfaces for military personnel in various roles (commanders, analysts, logistics officers, etc.) who may have varying levels of technical expertise.
        Compliance with Military Standards: Ensure all software development follows applicable military protocols, coding standards, and regulations (e.g., DoD directives, NATO standards, or specific service branch requirements).
        Your task is to deliver a prototype or proof of concept for a specific application, such as a real-time mission coordination tool, a logistics management platform, or a secure communication system. Outline the software architecture, choose the appropriate technologies (programming languages, frameworks, and databases), and provide an implementation plan that includes testing, deployment, and integration with other military systems.

        Make sure your design also includes provisions for:

        Interoperability with other military applications, both within your branch and with allied forces.
        Data Integrity to ensure that mission-critical data is accurate and reliable, even when systems face hardware malfunctions or cyber attacks.
        Future Scalability to allow for additional functionality or expansion without significant redesign.
        Provide a detailed timeline for development, testing, and deployment, along with risk assessment and mitigation strategies for any potential challenges that may arise during the implementation phase.''',

        """,
        # tools=[tool2],
        llm= llm2,
        allow_delegation=False,
        max_iter=5  
    )
def create_researcher_agent(topic):
    return Agent(
        role='Researcher',   
        goal=f'Analyze the research papers and articles to extract key points and provide solution to the {topic}.',
        verbose=True,
        memory=False,
        cache = False,
        backstory="""You're a Researcher aimed to research on {topic} and provide effective solutions for it.
        You're responsible for reasoning the Research papers, and articles from wikipidia or professional sites to find best possible solution about {topic} .
        """,
        tools=[tool2],
        llm=llm,
        allow_delegation=True,
        max_iter=5
    )
# def create_analyst_agent(topic):
#     return Agent(
#         role='Analyst',   
#         goal=f'Analyze the Researcher response and extract key threads from that.',
#         verbose=True,
#         memory=False,
#         cache = False,
#         backstory="""You're a data analyst.
#         You're responsible for reasoning the Researcher's data, finding key problem areas from that .
#         You're currently working on a project to Suggest remedial measures for problem areas you found from Researchers response.""",
#         tools=[tool2],
#         llm=llm2,
#         allow_delegation=True,
#         max_iter=5
#     )

def create_news_expert_agent(topic):
    return Agent(
        role='News Expert',
        goal=f'Generate the latest news about {topic} from the news links of USA news reporters or channels through the internet.',
        verbose=True,
        memory=False,
        backstory = f"""
        You are a News Expert. Your job is to gather the latest news about "{topic}" from credible news channels and online sources using an internet search tool.

        You must explore a maximum of 10 relevant news articles that provide deep insight into the topic. After collecting the information, identify the key problem areas and suggest practical remedial measures based on your analysis.

        IMPORTANT: When using the internet search tool ("Search the internet with Serper"), you must pass your search as a plain string — for example: 'latest news on {topic}'. Do not format it as a dictionary, JSON, or structured input.

        Stick to reliable U.S.-based news sources if possible, and summarize the results clearly and concisely.
        """,
        tools=[tool2],
        llm=llm,
        allow_delegation=False,
        max_iter=5
    )
