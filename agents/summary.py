from utils.llm import llm

def summary_agent(state):
    """
    The Summary Agent creates a concise executive summary of the research paper based on the analysis.
    It condenses the key points into a 150-200 word overview that captures the essence of the paper,
    including the main objectives, methods, findings, and implications. This summary serves as a
    quick reference for readers who need to understand the paper's content without reading the full text.
    """
    print("📝 Summary Agent: Creating executive summary...")
    analysis = state["analysis"]

    response = llm.invoke(f"""
    Write a 150-200 word executive summary:
    {analysis}
    """)

    return {"summary": response.content}