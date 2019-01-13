from rasa_nlu.model import Metadata, Interpreter
import json

def pprint(o):
    ''' helper function to make dict dumps prettier'''
    print(json.dumps(o, indent=2))

# loading the rasa_nlu model
interpreter = Interpreter.load('./models/current/nlu')

# interpreting the result
result = interpreter.parse(u"Hello domino")
intent_final = result["intent"]["name"]

# displaying the result
print("*"*15)
print("INTENT:", str(intent_final))