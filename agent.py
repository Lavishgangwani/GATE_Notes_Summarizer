# import os
# from unittest import result
# from dotenv import load_dotenv
# from flask import json
# from crewai import Agent, Task, Crew, Process
# from extract_data import extract_syllabus_tool_func 
# from crewai import LLM
# from crewai.tools import tool
# load_dotenv()


# gemini_api_key = os.getenv("GEMINI_API_KEY")


# gemini_llm=LLM(
#     model="gemini/gemini-2.5-flash",  # Using latest Gemini 2.5 Pro
#     api_key=gemini_api_key,
#     temperature=0.7,
#     top_p=0.9,
#     max_tokens=2048)

# @tool("Google Search Tool")
# def search_topics(topic: str) -> str:
#     """
#     A simple web search tool that uses Serper API to fetch search results.
#     """
#     mock_search_results = {
#         "Machine Learning": "Machine Learning is a field of AI that focuses on building systems that learn from data.",
#         "Data Science": "Data Science involves extracting insights from structured and unstructured data.",
#         "Neural Networks": "Neural Networks are computing systems inspired by the biological neural networks that constitute animal brains.",
#         "Probability": "Probability is a branch of mathematics concerned with the analysis of random phenomena.",
#         "Statistics": "Statistics is the discipline that concerns the collection, organization, analysis, interpretation, and presentation of data.",
#         "Linear Algebra": "Linear Algebra is the branch of mathematics concerning"
#     }
#     return json.dumps(mock_search_results, indent=4)




# research_agent = Agent(
#     role="Research Topics Agent",
#     goal="Research all the topics extracted from the syllabus PDF and summarize them effectively. With proper example and formulas where needed.",
#     backstory="""You are an expert researcher in educational topics. 
#     You can take a list of topics, research them using web search, and provide detailed summaries with examples and formulas where needed.""",
#     tools=[search_topics, extract_syllabus_tool_func],
#     verbose=True,
#     allow_delegation=False,
#     llm=gemini_llm,
#     memory=False
# )

# write_agent=Agent(
#     role="Content Writing Agent",
#     goal="write each topic in detail. and summarize them effectively. With proper example and formulas where needed.",
#     backstory="""You are an expert in writing educational content. 
#     You can take a list of topics and create detailed explanations, summaries, examples, and formulas for each topic.
#     give me proper structure content topics""",
#     tools=[search_topics, extract_syllabus_tool_func],
#     verbose=True,
#     allow_delegation=False,
#     llm=gemini_llm,
#     memory=False
# )




# research_topics_task = Task(
#     description="""Extract all the topics from the syllabus PDF located at {location}.
#     The output should be a JSON object containing the extracted topics. and summarize them effectively. With proper example and formulas where needed.""",
#     expected_output="""A JSON object with the extracted topics, where keys are the main topics 
#     and values are lists of sub-topics. and a summarized research content.""",
#     agent=research_agent,
#     async_execution=False
# )

# write_topics_task = Task(
#     description="""Write detailed explanations for each topic extracted from the syllabus.
#     The output should be a comprehensive document covering all topics with examples and formulas where needed.""",
#     expected_output="""A detailed document covering all topics with explanations, examples, and formulas where needed. and give the proper structure content.""",
#     agent=write_agent,
#     async_execution=False
# )


# research_crew = Crew(
#     agents=[research_agent, write_agent],
#     tasks=[research_topics_task, write_topics_task],
#     process=Process.sequential,
#     verbose=True,
#     memory=False
# )

# def run_research_pipeline(path: str) -> str:
#     """
#     Execute the complete research pipeline.
#     """
#     try:
#         result = research_crew.kickoff(inputs={"location": path})
#         if hasattr(result, "output"):
#             blog_contain = result.output
#         else:
#             blog_contain = str(result)

#         return blog_contain
    
#     except Exception as e:
#         print(f"Error during pipeline execution: {str(e)}")
#         import traceback
#         traceback.print_exc()
#         raise




# if __name__ == "__main__":
#     try:
#         path="C:\\Users\\admin\\Desktop\\projects\\project1\\DA_2026_Syllabus.pdf"
#         research_result = run_research_pipeline(path)
        
#         output_filename = "research_summary.md"
#         with open(output_filename, "w", encoding="utf-8") as f:
#             f.write(research_result)
        
#         print(f"\n Research summary saved to: {output_filename}")
#         print(f"\n Preview:\n{research_result[:500]}...")
    
#     except Exception as e:
#         print(f"Failed to generate research summary: {str(e)}")
#         import traceback
#         traceback.print_exc()





import os
import json
import pdfplumber
import re
from dotenv import load_dotenv
from flask import json
from crewai import Agent, Task, Crew, Process
from crewai import LLM
from crewai.tools import tool
from extract_data import extract_syllabus_pdf

load_dotenv()


# ==================== CREWAI TOOLS ====================

@tool("Extract Syllabus Tool")
def extract_syllabus_tool_func(location: str) -> str:
    """
    Extracts the syllabus from a PDF file and returns JSON format.
    """
    extracted_data = extract_syllabus_pdf(location)
    result = {
        "Course Topics": extracted_data,
        "total_sections": len(extracted_data)
    }
    return json.dumps(result, indent=2)


@tool("Google Search Tool")
def search_topics(topic: str) -> str:
    """
    A web search tool that fetches search results for topics.
    Returns mock data for demonstration (replace with real API if needed).
    """
    mock_search_results = {
        "Machine Learning": "Machine Learning is a field of AI that focuses on building systems that learn from data. It encompasses supervised learning, unsupervised learning, and reinforcement learning.",
        "Data Science": "Data Science involves extracting insights from structured and unstructured data using statistical methods and programming.",
        "Neural Networks": "Neural Networks are computing systems inspired by biological neural networks. They consist of interconnected nodes (neurons) organized in layers.",
        "Probability": "Probability is a branch of mathematics concerned with the analysis of random phenomena. Formula: P(A) = favorable outcomes / total outcomes",
        "Statistics": "Statistics is the discipline concerned with collection, organization, analysis, interpretation, and presentation of data.",
        "Linear Algebra": "Linear Algebra is the branch of mathematics concerning vectors, matrices, and linear transformations. Essential for machine learning and data science.",
        "Python Programming": "Python is a high-level programming language widely used in data science and AI applications.",
        "Data Visualization": "Data Visualization involves representing data in graphical form to communicate insights effectively."
    }
    
    # Try to find relevant result for the topic
    for key, value in mock_search_results.items():
        if topic.lower() in key.lower() or key.lower() in topic.lower():
            return json.dumps({"topic": topic, "result": value}, indent=2)
    
    # Default response if no match
    return json.dumps({"topic": topic, "result": f"Information about {topic} is available"}, indent=2)


# ==================== CREWAI CONFIGURATION ====================

gemini_api_key = os.getenv("GEMINI_KEY_1")

gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=gemini_api_key,
    temperature=0.7,
    top_p=0.9,
    max_tokens=2048
)


# ==================== AGENTS ====================

research_agent = Agent(
    role="Research Topics Agent",
    goal="Extract and research all topics from the syllabus PDF. Provide comprehensive summaries with examples and formulas.",
    backstory="""You are an expert researcher in educational topics. 
    You extract topics from syllabi, research them thoroughly, and provide detailed summaries with practical examples and relevant formulas.""",
    tools=[search_topics, extract_syllabus_tool_func],
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    memory=False
)


write_agent = Agent(
    role="Content Writing Agent",
    goal="Create detailed, well-structured educational content for each topic with examples and formulas.",
    backstory="""You are an expert educational content writer. 
    You take topics and create comprehensive explanations with examples, formulas, and proper structure.
    You organize content in a clear, hierarchical manner suitable for learning.""",
    tools=[search_topics, extract_syllabus_tool_func],
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    memory=False
)


# ==================== TASKS ====================

research_topics_task = Task(
    description="""Extract all topics from the syllabus PDF at '{location}'.
    For each topic, provide:
    1. Clear topic name
    2. Related subtopics
    3. Brief research summary
    4. Key formulas or concepts where applicable
    
    Output as structured JSON.""",
    expected_output="""JSON object with extracted topics organized by sections.
    Include research summaries, examples, and relevant formulas for each topic.""",
    agent=research_agent,
    async_execution=False
)


write_topics_task = Task(
    description="""Using the topics from the research phase, write detailed educational content.
    For each topic:
    1. Write a comprehensive explanation
    2. Include practical examples
    3. Add relevant formulas with explanations
    4. Provide learning objectives
    5. Suggest related concepts
    
    Structure the content in a clear, hierarchical format suitable for studying.""",
    expected_output="""A well-structured markdown document with:
    - Clear section headings
    - Detailed explanations for each topic
    - Practical examples
    - Formulas with derivations where applicable
    - Summary points
    - Links between related topics""",
    agent=write_agent,
    async_execution=False
)


# ==================== CREW ====================

research_crew = Crew(
    agents=[research_agent, write_agent],
    tasks=[research_topics_task, write_topics_task],
    process=Process.sequential,
    verbose=True,
    memory=False
)


# ==================== PIPELINE EXECUTION ====================

def run_research_pipeline(pdf_path: str) -> str:
    """
    Execute the complete research and content generation pipeline.
    
    Args:
        pdf_path: Path to the syllabus PDF file
    
    Returns:
        Generated educational content as string
    """
    try:
        print(f"Starting pipeline with PDF: {pdf_path}")
        
        # Verify file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Execute crew
        result = research_crew.kickoff(inputs={"location": pdf_path})
        
        # Extract output
        if hasattr(result, "output"):
            content = result.output
        else:
            content = str(result)
        
        return content
    
    except FileNotFoundError as e:
        print(f"File Error: {str(e)}")
        raise
    except Exception as e:
        print(f"Pipeline Error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise


# ==================== MAIN EXECUTION ====================

if __name__ == "__main__":
    try:
        # Update this path to your actual PDF location
        pdf_path = "C:\\Users\\admin\\Desktop\\projects\\project1\\DA_2026_Syllabus.pdf"
        
        # Run the pipeline
        research_result = run_research_pipeline(pdf_path)
        
        # Save output to file
        output_filename = "research_summary.md"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(research_result)
        
        print(f"\nRearch summary saved to: {output_filename}")
        print(f"Preview (first 500 characters):\n{research_result[:500]}...\n")
    
    except Exception as e:
        print(f"Failed to generate research summary: {str(e)}")
        import traceback
        traceback.print_exc()