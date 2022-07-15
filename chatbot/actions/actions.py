from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests


class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        senderid= tracker.sender_id
        url = "https://graph.facebook.com/"+ senderid + "?fields=first_name,last_name,profile_pic&access_token=EAAhAlbxX4csBAJZBIIUd0xkiaD8UEeKpOvhqCQM9nMZAybu8zQtXsTDzblTD54akGin1bYyOEgE6uRoVPZAofR13WKthkDev02hMmP06WE87Ia1w7olYhtuCjwRGJiXVxZBCPz7uCqWU3nAOonIXmXbd7Tux9rSYI9v20KKP8eHvUak4ZBCbclZAMUIwRGAKihchKCPxe5DgZDZD"
        userid = requests.get(url)
        userid= userid.json()
        dispatcher.utter_message("hi " +userid["first_name"]+" I am  a virtual assistance how may i help you")



        return []