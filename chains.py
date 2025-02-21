import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from prompts import MEDICINE_EXTRACTION_PROMPT, MEDICINE_TRANSLATION_PROMPT

# Load environment variables
load_dotenv()

# Define prompts
medicine_extraction_prompt = ChatPromptTemplate.from_messages([
    ("system", MEDICINE_EXTRACTION_PROMPT),
    ("user", "Extract the medicines from the following prescription: {prescription}")
])

medicine_translation_prompt = ChatPromptTemplate.from_messages([
    ("system", MEDICINE_TRANSLATION_PROMPT),
    ("user", "Provide the salt profile of the following medicines: {medicines}")
])

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Create chains
medicine_extraction_chain = medicine_extraction_prompt | llm
medicine_translation_chain = medicine_translation_prompt | llm