from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

medbridge_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a medical prescriptor translator tool. Generat result after translating the prescription into normal human language",
            "Always provide detailed result, including requests for length, prescription, salt,etc.",

        ),
        MessagesPlaceholder(variable_name="messages"),
    ] 

)

generate_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful and accurate medical translator. Translate the doctor's message from doctor language to patient language. Maintain the medical context and terminology, but also ensure the patient can understand the message. If necessary, explain complex medical terms in simpler language for the patient.  If you are unsure of a term, ask for clarification."
            "Generate the accuarte translation possible."
            "If the user provide something that is not prescription, respond with a revised version of your previous attempts",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


llm = ChatOpenAI()
generate_chain = generate_prompt | llm
medbridge_chain = medbridge_prompt | llm