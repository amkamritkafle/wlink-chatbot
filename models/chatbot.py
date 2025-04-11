from langchain.chains import ConversationChain
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()  

# Initialize OpenAI model (GPT)
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize conversation chain with LangChain
conversation = ConversationChain(llm=llm)

def get_response(user_input):
    return conversation.predict(input=user_input)
