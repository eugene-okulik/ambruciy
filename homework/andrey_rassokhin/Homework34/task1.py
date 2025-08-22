from datetime import datetime
from time import sleep
import requests

while True:
    temperature = requests.get('https://wttr.in/Saint-Petersburg?format=%t').text
    print(datetime.now())
    print(f'Now temperature in Saint-Petersburg: {temperature}')
    sleep(2)
