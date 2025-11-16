import os
import time
import json
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

# ============================================================
# 🔧 Load environment variables
# ============================================================

load_dotenv()

# Example .env:
# GEMINI_KEY_1=AIzaSyA123...
# GEMINI_KEY_2=AIzaSyB456...

# ============================================================
# 🔒 Safe Gemini LLM Factory (Each key tied to one agent)
# ============================================================

def create_llm_with_retry(api_key: str, model_name: str = "gemini/gemini-2.5-flash"):
    """Create an LLM instance with retry handling for transient Gemini errors."""
    def llm_call(prompt: str, max_retries: int = 3):
        for attempt in range(1, max_retries + 1):
            try:
                llm = LLM(
                    model=model_name,
                    api_key=api_key,
                    temperature=0.7,
                    top_p=0.9,
                    max_tokens=2048
                )
                return llm.call(prompt)

            except Exception as e:
                err = str(e).lower()

                # Retry only for transient issues (503, rate limit)
                if "503" in err or "overloaded" in err or "rate limit" in err:
                    wait = 5 * attempt
                    print(f"⚠️ Gemini API overloaded (attempt {attempt}) — retrying in {wait}s...")
                    time.sleep(wait)
                    continue

                elif "invalid api key" in err or "unauthorized" in err:
                    print("❌ Invalid or expired Gemini API key.")
                    break

                else:
                    print(f"❌ Non-retryable LLM error: {e}")
                    break

        raise RuntimeError(f"Gemini API failed after {max_retries} attempts.")
    return llm_call

# ============================================================
# 🔑 Assign one key per agent
# ============================================================

GEMINI_KEY_1 = os.getenv("GEMINI_KEY_1")
GEMINI_KEY_2 = os.getenv("GEMINI_KEY_2")

if not GEMINI_KEY_1 or not GEMINI_KEY_2:
    raise EnvironmentError("❌ Missing GEMINI_KEY_1 or GEMINI_KEY_2 in your .env file")

llm_agent1 = create_llm_with_retry(GEMINI_KEY_1)
llm_agent2 = create_llm_with_retry(GEMINI_KEY_2)

# ============================================================
# 🧠 Define Tools (Optional Example)
# ============================================================

@tool("Extract Syllabus Tool")
def extract_syllabus_tool(pdf_path: str) -> dict:
    """Dummy tool placeholder (replace with your actual syllabus extractor)."""
    return {
        "status": "success",
        "message": f"Syllabus extracted successfully from {pdf_path}"
    }

# ============================================================
# 🤖 Define Agents (Each uses its own LLM)
# ============================================================

research_agent_1 = Agent(
    name="Research Agent 1 - Part A",
    role="Researcher for first half of topics",
    goal="Extract and analyze Part A topics from the syllabus PDF.",
    backstory="Expert in foundational topics with academic research experience.",
    llm=llm_agent1,
    tools=[extract_syllabus_tool],
    verbose=True
)

research_agent_2 = Agent(
    name="Research Agent 2 - Part B",
    role="Researcher for second half of topics",
    goal="Extract and analyze Part B topics from the syllabus PDF.",
    backstory="Expert in advanced mathematical and engineering subjects.",
    llm=llm_agent2,
    tools=[extract_syllabus_tool],
    verbose=True
)

# ============================================================
# 🧾 Define Tasks
# ============================================================

task_a = Task(
    description=(
        "Analyze the first half of the syllabus and summarize the key concepts, "
        "prerequisites, and learning objectives. Include formulas and real-world examples."
    ),
    agent=research_agent_1,
    expected_output="Structured JSON with Part A topics, subtopics, and summaries."
)

task_b = Task(
    description=(
        "Analyze the second half of the syllabus and summarize the key concepts, "
        "applications, and mathematical relationships. Include formulas and examples."
    ),
    agent=research_agent_2,
    expected_output="Structured JSON with Part B topics, subtopics, and summaries."
)

# ============================================================
# 🚀 Crew Setup and Execution
# ============================================================

crew = Crew(
    agents=[research_agent_1, research_agent_2],
    tasks=[task_a, task_b],
    process=Process.sequential,
    verbose=True
)

def run_pipeline():
    try:
        print("\n🚀 Starting Research Crew Execution...\n")
        result = crew.run()
        print("\n✅ Research completed successfully.\n")
        return result
    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
        raise

# ============================================================
# 🏁 Main
# ============================================================

if __name__ == "__main__":
    output = run_pipeline()
    with open("research_output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print("📄 Output saved to research_output.json")
