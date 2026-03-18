from utils.llm import llm

def analyzer_agent(state):
    """
    The Analyzer Agent is responsible for extracting key components from the research paper text.
    It identifies and summarizes the problem statement, methodology used in the research,
    and the key findings or results presented in the paper. This agent provides a structured
    breakdown of the paper's core elements to facilitate further analysis and summarization.
    """
    print("🔍 Analyzer Agent: Analyzing the paper...")
    text = state["paper_text"]

    response = llm.invoke(f"""
    Extract the following from the research paper:
    - Problem statement
    - Methodology
    - Key findings
    
    Paper:
    {text[:8000]}
    """)

    return {"analysis": response.content}