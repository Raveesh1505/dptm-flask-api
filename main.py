import os
from typing import List, Sequence
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph


from chains import generate_chain, medbridge_chain

MEDBRIDGE = "medbridge"
GENERATE = "generate"

def generation_node(state: Sequence[BaseMessage]):
    return generate_chain.invoked({"message":state})


def medbridge_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = medbridge_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]


builder = MessageGraph()
builder.add_node(GENERATE, generation_node)
builder.add_node(MEDBRIDGE, medbridge_node)
builder.set_entry_point(GENERATE)

def should_continue(state: List[BaseMessage]):
    if len(state) > 6:
        return END
    return MEDBRIDGE

builder.add_conditional_edges(GENERATE, should_continue)
builder.add_edge(MEDBRIDGE, GENERATE)

graph = builder.compile()
print(graph.get_graph().draw_mermaid())
graph.get_graph().print_ascii()


if __name__ == "__main__":
    print("Hello LangGraph")
    inputs = HumanMessage(content="""Make this translation better:"
                          @LangChainAI
             - newly Tool Calling feature is seriously underrated.
                          """)
response = graph.invoke(inputs)
