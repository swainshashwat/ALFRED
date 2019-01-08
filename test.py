from rasa_nlu.model import Interpreter
import json
#import pyttsx

interpreter = Interpreter.load("./models/current/nlu")
message = "tenks"
result = interpreter.parse(message)
reply = json.dumps(result, indent=0)
#print(reply)
print(result["intent"]["name"])
#print(type(reply))
