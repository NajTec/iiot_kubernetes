import requests
import json
import datetime
import random



x = datetime.datetime.now()
n = random.randint(1,12)
f = random.random()
url = "http://python-klr-service.default.18.117.24.35.sslip.io"
payload = {}
payload["timestamp"] = str(x)
payload["temp"] = f
payload["device"] = n 

  
response = requests.get(url, json = payload)

