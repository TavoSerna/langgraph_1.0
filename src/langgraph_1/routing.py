from langgraph.graph import END, MessagesState

def should_continue(state: MessagesState) -> str:
    if state["messages"][-1].tool_calls:
        return "act"
    return END