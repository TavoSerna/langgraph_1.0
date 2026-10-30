from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from langgraph_1.react import llm,tools

SYSTEM_MESSAGE = """
You are a hepful assistant that can use tools to answer questions.
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    """
    response = llm.invoke([{"role":"system","content": SYSTEM_MESSAGE}, *state['messages']])
    return {"messages":[response]}

tool_node = ToolNode(tools)
