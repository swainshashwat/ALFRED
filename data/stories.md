## greeting
* greet
    - utter_greet

## goodbye
* goodbye
    - utter_goodbye

## ask weather [reply location?]
* ask_weather
    - utter_ask_location

## ask weather [reply weather info]
* ask_weather
    - action_weather## Generated Story -6533858942375851734
* greet
    - utter_greet
* ask_weather
    - utter_ask_location
* ask_weather{"location": "london"}
    - slot{"location": "london"}
    - action_weather
* goodbye
    - utter_goodbye

