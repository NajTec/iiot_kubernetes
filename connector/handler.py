import json
import datetime
import requests
def endpoint(event, context):
  password = "OeKbgKDYJgGnEnaKknED"
  auth_url = 'http://a9cea8116617a43c59acc7f03669c088-1194859127.us-east-2.elb.amazonaws.com:8081/v1/auth'
  auth_data = {"username":"demo-superuser","password":password}
  y = requests.post(auth_url,json=auth_data,headers={"Content-Type":"application/json"})
  url = 'http://a9cea8116617a43c59acc7f03669c088-1194859127.us-east-2.elb.amazonaws.com:8082/v2/keyspaces/temp/tempdata' 
  auth_token = json.loads(y.text)
 
  x = requests.post(url, json = event, headers = {"X-Cassandra-Token": auth_token["authToken"],"Content-Type":"application/json"})

  response = {
      "statusCode": 200,
      "body" : auth_token["authToken"]
  }
  return response
