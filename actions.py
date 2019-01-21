from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action, Tracker
from rasa_core.events import SlotSet

class ActionWeather(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '7408bba18ee2456cac1115352192101'
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temp_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment.\
                    The temperature is {} degrees,\
                    the humidity is {} percent \
                    and the wind speed is {} mph""".format(condition,
                     city, temp_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]

        