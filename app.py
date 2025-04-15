import streamlit as st
from crews import create_crews
import dotenv
import time
import os

dotenv.load_dotenv()
st.set_page_config(layout="wide")
def main():

    st.markdown(
        """
        <style>
        
        .main {
            background-color: blue;
            font-family: 'Arial', sans-serif;
        }
       
        section[data-testid="stSidebar"] {
            background-color: gray;
            input-color: rainyblue;
        }

        input{
            background-color: rainyblue !important;  /* Light Blue */
            # padding: 10px !important;
            # margin-bottom: 20px !important;
            # border-radius: 5px !important;
            # border: 1px solid #ccc !important;
        } 
        body {
            background-color: white;
        }
        .output-section {
            background-color: white;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .title {
            background-color: gray; 
            color: whitesmoke;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }
        .developer-banner {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: rgba(128, 128, 128, 0.8);
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 14px;
        z-index: 999;
    }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title"><h1>Research and Analysis System 🤖</h1></div>', unsafe_allow_html=True)

    st.markdown("""
        Welcome to the **Multi-Agent Research and Analysis System**. 
        Enter the task you want the agents to execute and the topic you're interested in. 
        You will receive a detailed and well-formatted report based on the results.
    """)

    st.sidebar.title("Task Settings")
    task_query = st.sidebar.text_input(f"**Enter the task** (e.g., research, news search):", value="news search")

    result_placeholder = st.empty()

    input_placeholder = st.empty()
    with input_placeholder:
        topic_input = st.text_input(f"**Enter the topic you want to explore:**", value="Russia Ukrain war")

    if st.button("Run Task"):
        crew1, crew2, crew3 = create_crews(topic_input)
        result = None  
        if any(word in task_query.lower() for word in ["code", "python"]):
            result_placeholder.markdown(f"🚀**Running Software_Expert on topic:**{topic_input}")
            result = crew1.kickoff(inputs={"topic": topic_input})

            if result: 
                task_outputs = result.tasks_output 
                progress = st.progress(0)  

                software_output = task_outputs[0]
                st.write(f"**Task**: {software_output.description}")
                st.markdown(f"**Expected Output**: {software_output.expected_output}")
                st.markdown(f"**Agent**: {software_output.agent}")
                st.write("---")
    
                st.markdown(software_output) 
                progress.progress(100) 
                time.sleep(2) 
                
                st.write("---")
                # st.write(f"###Analysis on the Researcher's Response")
                
                # analyst_output = task_outputs[1]
                # st.write(f"**Task**: {analyst_output.description}")
                # st.markdown(f"**Expected Output**: {analyst_output.expected_output}")
                # st.markdown(f"**Agent**: {analyst_output.agent}")
                # st.write("---")
    
                # st.markdown(analyst_output) 
                # progress.progress(100) 
            result_placeholder.success("Research and Analysis Task Completed!")
        
        elif any(word in task_query.lower() for word in ["internet", "news", "article", "trending news"]):
            result_placeholder.markdown(f"Running Internet Search on topic: {topic_input}")
            result = crew2.kickoff(inputs={"topic": topic_input})
            if result:  
                task_outputs = result.tasks_output  
    
                progress = st.progress(0) 

                news_output = task_outputs[0]
                st.write(f"**Task**: {news_output.description}")
                st.markdown(f"**Expected Output**: {news_output.expected_output}")
                st.markdown(f"**Agent**: {news_output.agent}")
                st.write("---")
    
                st.markdown(news_output) 
                progress.progress(100)  
            result_placeholder.success("News Reporter Task Completed!")

        elif any(word in task_query.lower() for word in ["research", "summarize", "analysis"]):
            result_placeholder.markdown(f"Running Researcher Agent")
            result = crew3.kickoff(inputs={"topic": topic_input})
            if result:  
                task_outputs = result.tasks_output  
    
                progress = st.progress(0) 

                researcher_output = task_outputs[0]
                st.write(f"**Task**: {researcher_output.description}")
                st.markdown(f"**Expected Output**: {researcher_output.expected_output}")
                st.markdown(f"**Agent**: {researcher_output.agent}")
                st.write("---")
    
                st.markdown(researcher_output) 
                progress.progress(100)  
            result_placeholder.success("Researcher Task Completed!")
        
        else:
            result_placeholder.markdown(f"Running Internet Search on topic: {topic_input}")
            result = crew2.kickoff(inputs={"topic": topic_input})
            if result:  
                task_outputs = result.tasks_output  
    
                progress = st.progress(0) 

                news_output = task_outputs[0]
                st.write(f"**Task**: {news_output.description}")
                st.markdown(f"**Expected Output**: {news_output.expected_output}")
                st.markdown(f"**Agent**: {news_output.agent}")
                st.write("---")
    
                st.markdown(news_output) 
                progress.progress(100)  
            result_placeholder.success("News Reporter Task Completed!")
            # In the style section, add these CSS rules:

# At the end of your main() function, just before the if __name__ == "__main__": line, add:
st.markdown('<div class="developer-banner">Developed by DGIS</div>', unsafe_allow_html=True)

        
# Run the Streamlit app
if __name__ == "__main__":
    main()
