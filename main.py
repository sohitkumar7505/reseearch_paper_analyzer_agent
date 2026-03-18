from graph import build_graph
from utils.pdf_loader import extract_text

def run(pdf_path):
    text = extract_text(pdf_path)

    graph = build_graph()
    state = {
        "paper_text": text,
        "analysis": "",
        "summary": "",
        "citations": "",
        "insights": "",
        "review_score": 0,
        "feedback": "",
        "verdict": "",
        "retry_count": 0
    }

    result = graph.invoke(state)
    print("Graph result keys:", list(result.keys()))
    # print("Full result:", result)
    if "final_output" in result:
        print(result["final_output"])
    else:
        print("No final_output key found")

if __name__ == "__main__":
    run("sample.pdf")