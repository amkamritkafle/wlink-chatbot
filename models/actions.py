# models/actions.py
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCustomResponse(Action):
    def name(self):
        return "action_custom_response"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        dispatcher.utter_message(text="This is a custom action response!")
        return []
