from typing import TypedDict
from langgraph.graph import StateGraph

from agents.analyzer import analyzer_agent
from agents.summary import summary_agent
from agents.citation import citation_agent
from agents.insights import insights_agent
from agents.reviewer import review_agent



class GraphState(TypedDict):
    paper_text: str
    analysis: str
    summary: str
    citations: str
    insights: str
    review_score: int
    feedback: str
    verdict: str
    retry_count: int
    final_output: str

def boss_agent(state):
    print("📌 Boss Agent: Starting workflow...")
    return state
def combine_agent(state):
    print("📌 Combine Agent: Combining results...")
    final_output = f"""
📌 FINAL RESEARCH BRIEF

🔍 Analysis:
{state.get("analysis")}

📝 Summary:
{state.get("summary")}

📚 Citations:
{state.get("citations")}

💡 Insights:
{state.get("insights")}
"""

    return {"final_output": final_output}
def review_analysis(state):
    print("🔍 Reviewing Analysis...")
    return review_agent(state, "analysis")


def review_summary(state):
    print("📝 Reviewing Summary...")
    return review_agent(state, "summary")


def review_citations(state):
    print("📚 Reviewing Citations...")
    return review_agent(state, "citations")


def review_insights(state):
    print("💡 Reviewing Insights...")
    return review_agent(state, "insights")



def should_retry(state):
    print(f"Review Score: {state['review_score']}")

    if state["review_score"] < 7 and state["retry_count"] < 2:
        print("🔁 Retrying...")
        state["retry_count"] += 1
        return "retry"

    print("✅ Approved")
    return "next"
def build_graph():
    builder = StateGraph(GraphState)

    # Nodes
    builder.add_node("boss", boss_agent)
    builder.add_node("combine", combine_agent)
    builder.add_node("analyzer", analyzer_agent)
    builder.add_node("review_analysis", review_analysis)

    builder.add_node("summary", summary_agent)
    builder.add_node("review_summary", review_summary)

    builder.add_node("citation", citation_agent)
    builder.add_node("review_citation", review_citations)

    builder.add_node("insights", insights_agent)
    builder.add_node("review_insights", review_insights)

    # Flow
    builder.set_entry_point("boss")
    builder.add_edge("boss", "analyzer")


    builder.add_edge("analyzer", "review_analysis")

    builder.add_conditional_edges(
        "review_analysis",
        should_retry,
        {
            "retry": "analyzer",
            "next": "summary"
        }
    )

    builder.add_edge("summary", "review_summary")
    builder.add_conditional_edges(
        "review_summary",
        should_retry,
        {
            "retry": "summary",
            "next": "citation"
        }
    )

    builder.add_edge("citation", "review_citation")
    builder.add_conditional_edges(
        "review_citation",
        should_retry,
        {
            "retry": "citation",
            "next": "insights"
        }
    )

    builder.add_edge("insights", "review_insights")
    builder.add_conditional_edges(
        "review_insights",
        should_retry,
        {
            "retry": "insights",
            "next": "combine"
        }
    )
    builder.add_edge("review_insights", "combine")
    builder.add_edge("combine", "__end__")
    return builder.compile()