import os

import rasa

from rasa.core.agent
import Agent

# No need to import policies directly in Rasa 3.x



class 
ChatRasa:

def
__init__(self):

# Set paths for Rasa model and NLU model

self.model_path
= 
"models/chatbot_model"
# Define where Rasa stores its models

self.agent
= 
None



# Initialize the agent and load pre-trained models

self.load_agent()



def
load_agent(self):

"""Load Rasa model and agent."""

try:

self.agent
= Agent.load(self.model_path)

print("Rasa agent loaded successfully.")

except
Exception
as e:

print(f"Error loading Rasa agent:
{e}")



def
get_response(self,
message):

"""Return the chatbot response."""

if
self.agent:

# Use the agent's interpreter to process the message

response =
self.agent.handle_text(message)

return response

else:

return
"Agent is not loaded properly, please check the configuration.