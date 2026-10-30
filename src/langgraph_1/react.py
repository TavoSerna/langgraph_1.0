from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun

@tool
def triple(num:float) -> float:
    """_summary_
    Args:
        num (float): a number to triple
    Returns:
        float: the triple of the input number 
    """
    return float(num) * 3

search = DuckDuckGoSearchRun(max_results=1)
tools = [search, triple]

llm = ChatOllama(model="qwen3:1.7b", temperature=0).bind_tools(tools=tools)



