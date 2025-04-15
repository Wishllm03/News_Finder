from crewai import Task
from tools import  tool2
from agents import create_software_agent, create_researcher_agent, create_news_expert_agent

def create_tasks(topic):
    software_task = Task(
        description=f"Give Python Program for {topic} with reliable, efficiant code example.",
        expected_output=f"A comprehensive paragraph of 600 words containing proper headings and their respective descriptions with the python code on the {topic} .",
        agent=create_software_agent(topic),  
        # tools=[tool2],
        output_file= "/research_report.md"
    )

   
    researcher_task = Task(
        agent=create_researcher_agent(topic),
        async_execution= True,
        description=f"Analyze and apply reasoning on Research Papers and articles about {topic} and extract key points and key solutions from that as a final report.",
        expected_output=(
            'A comprehensive paragraph of 500 words with proper bold headings and descriptions in points as the following: '
            '"Key Researches": list top 5 researches in 150 words, '
            '"Diagram": Draw an effective diagram demonstrating workflow of the {topic}'
            '"Key Suggations":  suggest about {topic} in 100 words after research and analysis from reasearch papers and articles in 150 words.'
            '"Refferences": Give resource references.'
            '"Summary of the Report": Summaries the analysis report in 100 words'
        ),
        # expected_output = "A comprehensive paragraph of 200 words containing key problem areas from Researcher\'s response and suggest remedial measures for those problems.",
        tools=[tool2],
        output_file = "/research_report.md"
    )
   
    news_task = Task(
        agent=create_news_expert_agent(topic),
        description=f"""find and generate the current date latest news about {topic} from appropriate News Channel's websites through the internet.
        Find Key-Problem Areas from the news gathered from the internet and suggest Remedial measures for that.
        Try to give the most recent news of current date reports and links.
        You have to only go through maximum 10 news links.""",
        expected_output=(
            'A comprehensive paragraph of 800 words containing headings and descriptions as the following: '
            '"Trending:": Elaborate Current date top 10 findings in detail in points in approx 500 words,'
            '"Key Threads": key problem areas for the current situation in 200 words, '
            '"My Openion": Suggest remedial measures for problems highlighted in 150 words,'
            '"News Links": Give atleast 10 news links that you find from internet in points'
        ),
        tools=[tool2],
        output_file="/Output.md"
    )

    return software_task, researcher_task, news_task
    
    # analyst_task = Task(
    #     agent=create_analyst_agent(topic),
    #     async_execution= True,
    #     description=f"Analyze and apply reasoning on the Researcher's response on {topic} and extract key threads from that as a final report.",
    #     expected_output=(
    #         'A comprehensive paragraph of 500 words with proper bold headings and descriptions in points as the following: '
    #         '"Key Threads": key problem areas from the researcher\'s response in 150 words, '
    #         '"Key Suggations": Suggest remedial measures for problems highlighted in 100 words.'
    #         '"News Links": Give resource links that you find through the internet search.'
    #         '"Summary of the Report": Summaries the analysis report in 100 words'
    #     ),
    #     # expected_output = "A comprehensive paragraph of 200 words containing key problem areas from Researcher\'s response and suggest remedial measures for those problems.",
    #     tools=[tool2],
    #     output_file = "/analysis_report.md"
    # )
