from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

# Initialize OpenAI model (GPT)
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Initialize conversation chain with LangChain
conversation = ConversationChain(llm=llm)

def get_response(user_input):
    return conversation.predict(input=user_input)
