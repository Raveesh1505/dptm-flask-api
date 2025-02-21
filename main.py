from typing import List, Sequence
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import medicine_extraction_chain, medicine_translation_chain
from prompts import TEST_MESSAGE

MEDICINE_EXTRACTION = "medicine_extraction"
MEDICINE_TRANSLATION = "medicine_translation"

def medicine_extraction_node(state: Sequence[BaseMessage]):
    return medicine_extraction_chain.invoke({"prescription": state})

def medicine_translation_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    result = medicine_translation_chain.invoke({"medicines": messages})
    return [HumanMessage(content=result.content)]

builder = MessageGraph()
builder.add_node(MEDICINE_EXTRACTION, medicine_extraction_node)
builder.add_node(MEDICINE_TRANSLATION, medicine_translation_node)
builder.set_entry_point(MEDICINE_EXTRACTION)
builder.add_edge(MEDICINE_EXTRACTION, MEDICINE_TRANSLATION)
builder.add_edge(MEDICINE_TRANSLATION, END)
graph = builder.compile()

if __name__ == "__main__":
    inputs = HumanMessage(content=TEST_MESSAGE)
    response = graph.invoke(inputs)