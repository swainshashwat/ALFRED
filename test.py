import re
import json
import os
import argparse
from datetime import datetime

from rasa_nlu.model import Interpreter
#import pyttsx

# Adding command line arguements
parser = argparse.ArgumentParser()
parser.add_argument("--model",
         help="model timestamp format - YearMonthDay-HourMinuteSecond",
         nargs="?", default="latest", const=0)
         
args = parser.parse_args()

# parsing command line arguemnts
# parsing model-no
model_no = ''
if args.model=="latest":
    dates = []
    re_date = r'\d{4}\d{2}\d{2}-\d{2}\d{2}\d{2}'
    for d in os.listdir("models"):
        re_date = datetime.strptime(
                re.search(re_date, d).group(),
                '%Y%m%d-%H%M%S')
        dates.append(re_date)
    model_no = max(dates)
    model_no = model_no.strftime('%Y%m%d-%H%M%S')
    model_name = 'model_' + model_no
else:
    model_no = args.model
    model_name = 'model_' + model_no
    if model_name not in os.listdir('models/'):
        raise Exception('FileNotFound: '+model_name+' does not exist')


interpreter = Interpreter.load(os.path.join('models', model_name))
message = "here's some kisses :*"
result = interpreter.parse(message)
reply = json.dumps(result, indent=0)
#print(reply)
print("*"*15)
print(result["intent"]["name"])
#print(type(reply))
