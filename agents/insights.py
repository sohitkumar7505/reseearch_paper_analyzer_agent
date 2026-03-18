from utils.llm import llm

def insights_agent(state):
    """
    The Insights Agent generates valuable insights and practical takeaways from the research paper's analysis.
    It identifies novel contributions, potential applications, limitations, and future research directions.
    This agent provides deeper understanding by highlighting the significance of the findings,
    their real-world implications, and actionable recommendations derived from the paper's content.
    """
    print("💡 Insights Agent: Generating insights...")
    analysis = state["analysis"]

    response = llm.invoke(f"""
    Generate key insights and practical takeaways:
    {analysis}
    """)

    return {"insights": response.content}