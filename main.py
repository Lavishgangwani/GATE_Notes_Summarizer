import os
import json
import pdfplumber
import re
from dotenv import load_dotenv
from flask import json
from crewai import Agent, Task, Crew, Process
from crewai import LLM
from crewai.tools import tool

load_dotenv()


# ==================== PDF EXTRACTION ====================

def extract_syllabus_pdf(pdf_path: str) -> dict:
    """
    Extract structured syllabus data from PDF file.
    Returns hierarchical topic structure with sections and subtopics.
    """
    extracted_data = {
        "title": "",
        "sections": [],
        "total_topics": 0
    }
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            
            # Extract text from all pages
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
            
            # Parse hierarchical structure
            lines = full_text.split('\n')
            current_section = None
            current_subsection = None
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Detect main sections (e.g., "1. Probability and Statistics")
                if re.match(r'^\d+\.\s+[A-Z]', line):
                    current_section = {
                        "name": line,
                        "subsections": []
                    }
                    extracted_data["sections"].append(current_section)
                
                # Detect subsections (e.g., "1.1 Counting Principles")
                elif re.match(r'^\d+\.\d+\s+', line) and current_section:
                    current_subsection = {
                        "name": line,
                        "topics": []
                    }
                    current_section["subsections"].append(current_subsection)
                
                # Detect topics (e.g., "1 Permutation and Combination")
                elif re.match(r'^\d+\s+[A-Z]', line) and current_subsection:
                    current_subsection["topics"].append(line)
                    extracted_data["total_topics"] += 1
            
            # Extract title from first few lines
            for line in lines[:10]:
                if line.strip() and len(line.strip()) > 10:
                    extracted_data["title"] = line.strip()
                    break
        
        return extracted_data
    
    except Exception as e:
        print(f"Error extracting PDF: {str(e)}")
        return extracted_data


def split_topics_into_halves(extracted_data: dict) -> tuple:
    """
    Split extracted topics into two halves for parallel processing.
    Returns (first_half, second_half) tuples.
    """
    all_topics = []
    
    # Flatten all topics
    for section in extracted_data.get("sections", []):
        for subsection in section.get("subsections", []):
            for topic in subsection.get("topics", []):
                all_topics.append({
                    "section": section["name"],
                    "subsection": subsection["name"],
                    "topic": topic
                })
    
    # Split into halves
    mid = len(all_topics) // 2
    first_half = all_topics[:mid]
    second_half = all_topics[mid:]
    
    return first_half, second_half


# ==================== CREWAI TOOLS ====================

@tool("Extract Syllabus Tool")
def extract_syllabus_tool_func(location: str) -> str:
    """
    Extracts the syllabus from a PDF file and returns JSON format.
    """
    try:
        extracted_data = extract_syllabus_pdf(location)
        result = {
            "status": "success",
            "title": extracted_data.get("title", "Untitled"),
            "sections": extracted_data.get("sections", []),
            "total_topics": extracted_data.get("total_topics", 0)
        }
        return json.dumps(result, indent=2)
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)}, indent=2)


@tool("Google Search Tool")
def search_topics(topic: str) -> str:
    """
    A web search tool that fetches search results for topics.
    Returns mock data for demonstration.
    """
    mock_search_results = {
        "Probability": "Probability is the measure of likelihood that an event will occur. P(A) = favorable outcomes / total outcomes.",
        "Statistics": "Statistics involves collection, analysis, interpretation of data using mathematical methods.",
        "Linear Algebra": "Linear Algebra studies vectors, matrices, and linear transformations fundamental to ML.",
        "Counting Principles": "Methods to count elements in finite sets including permutations and combinations.",
        "Distributions": "Mathematical functions describing probabilities of outcomes for random variables.",
        "Eigenvalues": "Scalar values representing the magnitude of eigenvectors in matrix transformations.",
        "Hypothesis Testing": "Statistical method to test claims about population parameters using sample data.",
        "Matrix Operations": "Computations involving matrices including addition, multiplication, and decomposition."
    }
    
    for key, value in mock_search_results.items():
        if topic.lower() in key.lower() or key.lower() in topic.lower():
            return json.dumps({"topic": topic, "result": value}, indent=2)
    
    return json.dumps({"topic": topic, "result": f"Information about {topic}"}, indent=2)


# ==================== CREWAI CONFIGURATION ====================

gemini_api_key1 = os.getenv("GEMINI_API_KEY")
gemini_api_key2 = os.getenv("GEMINI_API_KEY_2")

gemini_llm1 = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=gemini_api_key1,
    temperature=0.7,
    top_p=0.9,
    max_tokens=2048
)

gemini_llm2 = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=gemini_api_key2,
    temperature=0.7,
    top_p=0.9,
    max_tokens=2048
)

# ==================== AGENTS ====================

research_agent_1 = Agent(
    role="Research Agent 1 - Part A Topics",
    goal="Extract and research the first half of topics from the syllabus PDF.",
    backstory="Expert researcher specializing in foundational concepts with deep analysis.",
    tools=[search_topics, extract_syllabus_tool_func],
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm1,
    memory=False
)

research_agent_2 = Agent(
    role="Research Agent 2 - Part B Topics",
    goal="Extract and research the second half of topics from the syllabus PDF.",
    backstory="Expert researcher specializing in advanced concepts with comprehensive coverage.",
    tools=[search_topics, extract_syllabus_tool_func],
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm2,
    memory=False
)

write_agent_1 = Agent(
    role="Content Writer 1 - Part A Documentation",
    goal="Create detailed educational content for part A topics with examples and formulas.",
    backstory="Educational content specialist for foundational materials with clear explanations.",
    tools=[search_topics, extract_syllabus_tool_func],
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm1,
    memory=False
)

write_agent_2 = Agent(
    role="Content Writer 2 - Part B Documentation",
    goal="Create detailed educational content for part B topics with examples and formulas.",
    backstory="Educational content specialist for advanced materials with comprehensive detail.",
    tools=[search_topics, extract_syllabus_tool_func],
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm2,
    memory=False
)

# ==================== TASKS ====================

research_task_1 = Task(
    description="""Extract and research FIRST HALF topics from PDF at {location}.
    For each topic provide:
    - Clear description and comprehensive explanation
    - Related subtopics and prerequisites
    - Detailed research summary with key concepts
    - Key formulas and mathematical concepts
    - Real-world applications and use cases
    - Learning difficulty level
    
    Output as structured JSON.""",
    expected_output="Detailed JSON with researched Part A topics including descriptions, formulas, prerequisites, applications, and difficulty levels.",
    agent=research_agent_1,
    async_execution=False
)

research_task_2 = Task(
    description="""Extract and research SECOND HALF topics from PDF at {location}.
    For each topic provide:
    - Clear description and comprehensive explanation
    - Related subtopics and prerequisites
    - Detailed research summary with key concepts
    - Key formulas and mathematical concepts
    - Real-world applications and use cases
    - Learning difficulty level
    
    Output as structured JSON.""",
    expected_output="Detailed JSON with researched Part B topics including descriptions, formulas, prerequisites, applications, and difficulty levels.",
    agent=research_agent_2,
    async_execution=False
)

write_task_1 = Task(
    description="""Create comprehensive educational content for Part A topics.
    For each topic create:
    - 300-500 word explanation
    - 3-5 practical real-world examples
    - Relevant formulas with step-by-step derivations
    - Clear learning objectives
    - Summary points and key takeaways
    - Common misconceptions and pitfalls
    
    Use proper markdown formatting with hierarchical headings.""",
    expected_output="Comprehensive markdown document for Part A with detailed explanations, examples, formulas, learning objectives, and key points.",
    agent=write_agent_1,
    async_execution=False
)

write_task_2 = Task(
    description="""Create comprehensive educational content for Part B topics.
    For each topic create:
    - 300-500 word explanation
    - 3-5 practical real-world examples
    - Relevant formulas with step-by-step derivations
    - Clear learning objectives
    - Summary points and key takeaways
    - Common misconceptions and pitfalls
    
    Use proper markdown formatting with hierarchical headings.""",
    expected_output="Comprehensive markdown document for Part B with detailed explanations, examples, formulas, learning objectives, and key points.",
    agent=write_agent_2,
    async_execution=False
)

# ==================== CREW ====================

research_crew = Crew(
    agents=[research_agent_1, research_agent_2, write_agent_1, write_agent_2],
    tasks=[research_task_1, research_task_2, write_task_1, write_task_2],
    process=Process.sequential,
    verbose=True,
    memory=False
)

# ==================== PIPELINE EXECUTION ====================

def run_research_pipeline(pdf_path: str) -> str:
    """
    Execute the complete research and content generation pipeline.
    
    Workflow:
    1. Extract and research Part A topics
    2. Extract and research Part B topics
    3. Generate content for Part A
    4. Generate content for Part B
    
    Args:
        pdf_path: Path to the syllabus PDF file
    
    Returns:
        Generated educational content as string
    """
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        print(f"\n{'='*80}")
        print("🚀 STARTING PIPELINE EXECUTION")
        print(f"{'='*80}\n")
        
        # Execute crew
        result = research_crew.kickoff(inputs={"location": pdf_path})
        
        # Extract output
        content = result.output if hasattr(result, "output") else str(result)
        
        print(f"\n{'='*80}")
        print("✅ PIPELINE EXECUTION COMPLETED SUCCESSFULLY")
        print(f"{'='*80}\n")
        
        return content
    
    except FileNotFoundError as e:
        print(f"\n❌ File Error: {str(e)}")
        raise
    except Exception as e:
        print(f"\n❌ Pipeline Error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise


# ==================== MAIN EXECUTION ====================

if __name__ == "__main__":
    try:
        # Update this path to your actual PDF location
        pdf_path = "Probability_and_LinearAlgebra_Complete_Topics.pdf"
        
        # Run the pipeline
        research_result = run_research_pipeline(pdf_path)
        
        # Save output to file
        output_filename = "research_summary.md"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(research_result)
        
        print(f"✅ Research summary saved to: {output_filename}")
        print(f"\nPreview (first 500 characters):\n{research_result[:500]}...\n")
    
    except Exception as e:
        print(f"\n❌ Failed to generate research summary: {str(e)}")
        import traceback
        traceback.print_exc()