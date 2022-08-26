import requests
import json
from random import randrange

password = "OeKbgKDYJgGnEnaKknED"
auth_url = 'http://localhost:8081/v1/auth'
auth_data = {"username":"demo-superuser","password":password}


def endpoint(event, context):
#	y = requests.post(auth_url,json=auth_data,headers={"Content-Type":"application/json"})
	#auth_token =  json.loads(y.text) 
	#print(auth_token)
	data = {
    		"timestamp": "12-21-2021:14:24",
    		"device": randrange(90),
    		"temp": 21.01
		}

#	header = "X-Cassandra-Token:cd95887c-4bf0-4bc1-9bec-45a8b8fd7f7d"
#	header1 = "Content-Type: application/json"
#	url = 'http://localhost:8082/v2/keyspaces/temp/tempdata'

#	x = requests.post(url, json = data, headers = {"X-Cassandra-Token": auth_token["authToken"],"Content-Type":"application/json"})

	return {"statusCode":200,"body": json.dumps({"message":"hello world"})}
