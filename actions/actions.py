# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from weather import Weather
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('GPE')
        temperature=Weather(city)['temp']
        response = "The current temperature at {} is {} degrees Celsius.".format(city,temperature)
        dispatcher.utter_message(response)

        return [SlotSet('GPE',city)]

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ent = tracker.get_latest_entity_values("sentiment", None)
        response = "Thank you for letting me know."
        if ent[0] == "pos":
            response = "I'm glad you thought so. Goodbye."
        elif ent[0] == "neg":
            response = "I'm sorry you had that experience."
        
        print(ent)
        dispatcher.utter_message(response)

        return []