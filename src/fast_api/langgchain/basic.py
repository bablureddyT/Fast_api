from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert Python teacher."
    ),
    (
        "human",
        "Explain {topic} for a beginner."
    ),
])

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "topic": "decorators"
})

print(type(result))
print(result)
