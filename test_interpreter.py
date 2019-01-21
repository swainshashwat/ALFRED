from rasa_nlu.model import Metadata, Interpreter
import json

def run_nlu():
    interpreter = Interpreter.load("./models/current/nlu/")
    print("Interpreter Model loaded...")
    while True:
        message = input()
        if message=='stop':
            print('Stopped listening...')
            break
        res = interpreter.parse(message)
        print(json.dumps(res))

run_nlu()