# import os
# import json
# import time
# import pdfplumber
# import re
# from dotenv import load_dotenv
# from flask import json
# from crewai import Agent, Task, Crew, Process
# from crewai import LLM
# from crewai.tools import tool
# from extract_data import extract_syllabus_pdf

# load_dotenv()


# # ==================== CREWAI TOOLS ====================

# @tool("Extract Syllabus Tool")
# def extract_syllabus_tool_func(location: str) -> str:
#     """
#     Extracts the syllabus from a PDF file and returns JSON format.
#     """
#     extracted_data = extract_syllabus_pdf(location)
#     result = {
#         "Course Topics": extracted_data,
#         "total_sections": len(extracted_data)
#     }
#     return json.dumps(result, indent=2)


# @tool("Google Search Tool")
# def search_topics(topic: str) -> str:
#     """
#     A web search tool that fetches search results for topics.
#     Returns mock data for demonstration (replace with real API if needed).
#     """
#     mock_search_results = {
#         "Machine Learning": "Machine Learning is a field of AI that focuses on building systems that learn from data. It encompasses supervised learning, unsupervised learning, and reinforcement learning.",
#         "Data Science": "Data Science involves extracting insights from structured and unstructured data using statistical methods and programming.",
#         "Neural Networks": "Neural Networks are computing systems inspired by biological neural networks. They consist of interconnected nodes (neurons) organized in layers.",
#         "Probability": "Probability is a branch of mathematics concerned with the analysis of random phenomena. Formula: P(A) = favorable outcomes / total outcomes",
#         "Statistics": "Statistics is the discipline concerned with collection, organization, analysis, interpretation, and presentation of data.",
#         "Linear Algebra": "Linear Algebra is the branch of mathematics concerning vectors, matrices, and linear transformations. Essential for machine learning and data science.",
#         "Python Programming": "Python is a high-level programming language widely used in data science and AI applications.",
#         "Data Visualization": "Data Visualization involves representing data in graphical form to communicate insights effectively."
#     }
    
#     for key, value in mock_search_results.items():
#         if topic.lower() in key.lower() or key.lower() in topic.lower():
#             return json.dumps({"topic": topic, "result": value}, indent=2)
    
#     return json.dumps({"topic": topic, "result": f"Information about {topic} is available"}, indent=2)


# # ==================== HELPER FUNCTION TO DIVIDE TOPICS ====================

# def divide_topics_equally(topics_data: dict) -> tuple:
#     """
#     Divides extracted topics equally between two agents.
    
#     Args:
#         topics_data: Dictionary containing extracted topics
    
#     Returns:
#         Tuple of (topics_part1, topics_part2) - two dictionaries with equal distribution
#     """
#     # Extract topics list
#     if isinstance(topics_data, dict) and "Course Topics" in topics_data:
#         topics_raw = topics_data["Course Topics"]
#     else:
#         topics_raw = topics_data
    
#     # Convert to list if it's a dictionary
#     if isinstance(topics_raw, dict):
#         topics_list = list(topics_raw.items())  # Convert dict to list of tuples
#         topics_dict = topics_raw  # Keep original for reference
#     elif isinstance(topics_raw, list):
#         topics_list = topics_raw
#         topics_dict = {i: item for i, item in enumerate(topics_raw)}
#     else:
#         topics_list = list(topics_raw)
#         topics_dict = {i: item for i, item in enumerate(topics_list)}
    
#     # Calculate midpoint
#     midpoint = len(topics_list) // 2
    
#     # Divide topics
#     part1_list = topics_list[:midpoint]
#     part2_list = topics_list[midpoint:]
    
#     # Convert back to original format
#     if isinstance(topics_raw, dict):
#         part1_dict = dict(part1_list)
#         part2_dict = dict(part2_list)
#     else:
#         part1_dict = [item[1] if isinstance(item, tuple) else item for item in part1_list]
#         part2_dict = [item[1] if isinstance(item, tuple) else item for item in part2_list]
    
#     topics_part1 = {
#         "Course Topics": part1_dict,
#         "total_sections": len(part1_list),
#         "part": "Part 1"
#     }
    
#     topics_part2 = {
#         "Course Topics": part2_dict,
#         "total_sections": len(part2_list),
#         "part": "Part 2"
#     }
    
#     print(f"\n📊 Topics divided:")
#     print(f"   Part 1 (Agent 1): {len(part1_list)} topics")
#     print(f"   Part 2 (Agent 2): {len(part2_list)} topics\n")
    
#     return topics_part1, topics_part2


# # ==================== CREWAI CONFIGURATION ====================

# gemini_api_key1 = os.getenv("GEMINI_KEY_1")
# gemini_api_key2 = os.getenv("GEMINI_KEY_2")

# gemini_llm1 = LLM(
#     model="gemini/gemini-2.5-flash",
#     api_key=gemini_api_key1,
#     temperature=0.7,
#     top_p=0.9,
#     max_tokens=2048
# )

# gemini_llm2 = LLM(
#     model="gemini/gemini-2.5-flash",
#     api_key=gemini_api_key2,
#     temperature=0.7,
#     top_p=0.9,
#     max_tokens=2048
# )


# # ==================== AGENTS ====================

# research_agent1 = Agent(
#     role="Research Topics Agent - Part 1",
#     goal="Extract and research assigned topics from the first half of syllabus. Provide comprehensive summaries with examples and formulas.",
#     backstory="""You are an expert researcher in educational topics. 
#     You extract topics from syllabi, research them thoroughly, and provide detailed summaries with practical examples and relevant formulas.""",
#     tools=[search_topics, extract_syllabus_tool_func],
#     verbose=True,
#     allow_delegation=False,
#     llm=gemini_llm1,
#     memory=False
# )

# research_agent2 = Agent(
#     role="Research Topics Agent - Part 2",
#     goal="Extract and research assigned topics from the second half of syllabus. Provide comprehensive summaries with examples and formulas.",
#     backstory="""You are an expert researcher in educational topics. 
#     You extract topics from syllabi, research them thoroughly, and provide detailed summaries with practical examples and relevant formulas.""",
#     tools=[search_topics, extract_syllabus_tool_func],
#     verbose=True,
#     allow_delegation=False,
#     llm=gemini_llm2,
#     memory=False
# )


# write_agent_1 = Agent(
#     role="Content Writing Agent - Part 1",
#     goal="Create detailed educational content for assigned topics from part 1 with examples and formulas.",
#     backstory="""You are an expert educational content writer specializing in technical topics.
#     You create comprehensive explanations with examples, formulas, and proper structure for assigned topics.""",
#     tools=[search_topics],
#     verbose=True,
#     allow_delegation=False,
#     llm=gemini_llm1,
#     memory=False
# )


# write_agent_2 = Agent(
#     role="Content Writing Agent - Part 2",
#     goal="Create detailed educational content for assigned topics from part 2 with examples and formulas.",
#     backstory="""You are an expert educational content writer specializing in practical applications.
#     You create comprehensive explanations with examples, formulas, and proper structure for assigned topics.""",
#     tools=[search_topics],
#     verbose=True,
#     allow_delegation=False,
#     llm=gemini_llm2,
#     memory=False
# )


# # ==================== CREW ====================

# def create_crew(topics_part1, topics_part2):
#     """
#     Creates a Crew instance with tasks that include topic divisions.
#     """
#     # Convert topics to string representation for task descriptions
#     topics_part1_str = str(topics_part1.get("Course Topics", topics_part1))
#     topics_part2_str = str(topics_part2.get("Course Topics", topics_part2))
    
#     # Create new task instances with updated descriptions
#     task1 = Task(
#         description=f"""Extract and research all topics from the FIRST HALF of the syllabus PDF at '{{location}}'.
#     Topics assigned to Part 1: {topics_part1_str}
    
#     For each topic, provide:
#     1. Clear topic name
#     2. Related subtopics
#     3. Brief research summary
#     4. Key formulas or concepts where applicable
    
#     Output as structured JSON.""",
#         expected_output="""JSON object with extracted topics from Part 1 organized by sections.
#     Include research summaries, examples, and relevant formulas for each topic.""",
#         agent=research_agent1,
#         async_execution=False
#     )
    
#     task2 = Task(
#         description=f"""Extract and research all topics from the SECOND HALF of the syllabus PDF at '{{location}}'.
#     Topics assigned to Part 2: {topics_part2_str}
    
#     For each topic, provide:
#     1. Clear topic name
#     2. Related subtopics
#     3. Brief research summary
#     4. Key formulas or concepts where applicable
    
#     Output as structured JSON.""",
#         expected_output="""JSON object with extracted topics from Part 2 organized by sections.
#     Include research summaries, examples, and relevant formulas for each topic.""",
#         agent=research_agent2,
#         async_execution=False
#     )
    
#     task3 = Task(
#         description=f"""Using the researched topics from PART 1, write detailed educational content.
#     Topics to cover: {topics_part1_str}
    
#     For each assigned topic:
#     1. Write comprehensive explanation
#     2. Include practical examples
#     3. Add relevant formulas with explanations
#     4. Provide learning objectives
    
#     Structure content in clear, hierarchical format.""",
#         expected_output="""Markdown document with detailed explanations, examples, formulas, and summary points for Part 1 topics.""",
#         agent=write_agent_1,
#         async_execution=False
#     )
    
#     task4 = Task(
#         description=f"""Using the researched topics from PART 2, write detailed educational content.
#     Topics to cover: {topics_part2_str}
    
#     For each assigned topic:
#     1. Write comprehensive explanation
#     2. Include practical examples
#     3. Add relevant formulas with explanations
#     4. Provide learning objectives
    
#     Structure content in clear, hierarchical format.""",
#         expected_output="""Markdown document with detailed explanations, examples, formulas, and summary points for Part 2 topics.""",
#         agent=write_agent_2,
#         async_execution=False
#     )
    
#     return Crew(
#         agents=[research_agent1, research_agent2, write_agent_1, write_agent_2],
#         tasks=[task1, task2, task3, task4],
#         process=Process.sequential,
#         verbose=True,
#         memory=False
#     )


# # ==================== PIPELINE EXECUTION ====================

# def run_research_pipeline(pdf_path: str, max_retries: int = 5, base_delay: int = 10) -> str:
#     """
#     Execute the complete research and content generation pipeline with exponential backoff.
    
#     Args:
#         pdf_path: Path to the syllabus PDF file
#         max_retries: Maximum number of retry attempts
#         base_delay: Initial delay in seconds (exponentially increases)
    
#     Returns:
#         Generated educational content as string
#     """
#     attempt = 0
#     topics_part1 = None
#     topics_part2 = None

#     while attempt <= max_retries:
#         try:
#             print(f"\n🚀 Starting pipeline with PDF: {pdf_path}")
#             print(f"🕒 Attempt {attempt + 1}/{max_retries + 1}\n")

#             if not os.path.exists(pdf_path):
#                 raise FileNotFoundError(f"PDF file not found: {pdf_path}")

#             # Extract topics first (only on first attempt)
#             if topics_part1 is None:
#                 print("📚 Extracting topics from syllabus...")
#                 extracted_topics = extract_syllabus_pdf(pdf_path)
#                 topics_data = {
#                     "Course Topics": extracted_topics,
#                     "total_sections": len(extracted_topics)
#                 }
                
#                 # Divide topics equally - first half to agent1, second half to agent2
#                 topics_part1, topics_part2 = divide_topics_equally(topics_data)
            
#             # Create crew with divided topics
#             research_crew = create_crew(topics_part1, topics_part2)
            
#             result = research_crew.kickoff(inputs={"location": pdf_path})

#             # Handle output type (CrewAI returns an object sometimes)
#             content = result.output if hasattr(result, "output") else str(result)
#             return content

#         except Exception as e:
#             error_str = str(e).lower()
#             print(f"Error on attempt {attempt + 1}: {e}")

#             # Retry only for specific transient errors
#             if any(code in error_str for code in ["503", "429", "quota", "overload", "timeout"]):
#                 delay = base_delay * (2 ** attempt)  # exponential backoff
#                 print(f"Transient error detected. Retrying in {delay} seconds...\n")
#                 time.sleep(delay)
#                 attempt += 1
#                 continue

#             # Other errors — not retryable
#             import traceback
#             traceback.print_exc()
#             raise

#     # If all retries fail
#     raise RuntimeError(f"🚨 Pipeline failed after {max_retries + 1} attempts due to repeated 503/overload errors.")


# # ==================== MAIN EXECUTION ====================

# if __name__ == "__main__":
#     try:
#         pdf_path = "C:\\Users\\admin\\Desktop\\projects\\project1\\DA_2026_Syllabus.pdf"
        
#         research_result = run_research_pipeline(pdf_path)
        
#         output_filename = "research_summary1.md"
#         with open(output_filename, "w", encoding="utf-8") as f:
#             f.write(research_result)
        
#         print(f"\nResearch summary saved to: {output_filename}")
#         print(f"Preview (first 500 characters):\n{research_result[:500]}...\n")
    
#     except Exception as e:
#         print(f"Failed to generate research summary: {str(e)}")
#         import traceback
#         traceback.print_exc()