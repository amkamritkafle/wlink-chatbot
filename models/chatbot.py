import os
import asyncio
import rasa
from rasa.core.agent import Agent

class ChatRasa:
    def __init__(self):
        self.model_path = "models/chatbot_model"
        self.agent = None

    async def load_agent(self):
        """Asynchronously load the Rasa agent."""
        try:
            self.agent = await Agent.load(self.model_path)
            print("Rasa agent loaded successfully.")
        except Exception as e:
            print(f"Error loading Rasa agent: {e}")

    async def get_response(self, message):
        """Asynchronously get a chatbot response."""
        if self.agent:
            responses = await self.agent.handle_text(message)
            return responses
        else:
            return "Agent is not loaded properly, please check the configuration."

# Sample usage
async def main():
    bot = ChatRasa()
    await bot.load_agent()
    res = await bot.get_response("hello")
    print(res)

if __name__ == "__main__":
    asyncio.run(main())
