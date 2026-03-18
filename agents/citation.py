from utils.llm import llm

def citation_agent(state):
    """
    The Citation Agent extracts and organizes all references and citations mentioned in the research paper.
    It identifies academic sources, previous works, and any bibliographic information cited throughout the text.
    This agent ensures that all external references are properly documented and presented in a clear,
    structured format for academic integrity and further research purposes.
    """
    print("📚 Citation Agent: Extracting citations...")
    text = state["paper_text"]

    response = llm.invoke(f"""
    Extract all citations and references clearly:
    {text[:8000]}
    """)

    return {"citations": response.content}