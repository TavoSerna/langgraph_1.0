from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph, END

from langgraph_1.nodes import run_agent_reasoning, tool_node
from langgraph_1.routing import should_continue


AGENT_REASON = "agent_reason"
ACT = "act"

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)   

flow.add_conditional_edges(AGENT_REASON, should_continue, {
    END: END,
    ACT: ACT
})

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()


if __name__ == "__main__":
    print("Hello ReAct LangGraph")
    app.get_graph().draw_mermaid_png(output_file_path="flow.png")