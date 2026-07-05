from langchain_groq import ChatGroq
from dotenv import load_dotenv
from prompt import *
from states import *
load_dotenv()






user_prompt="create simple calculator web application"

prompt = planner_prompt(user_prompt)



llm= ChatGroq(model="openai/gpt-oss-120b")
response = llm.with_structured_output(schema=Plan).invoke(prompt)


print(response) 
