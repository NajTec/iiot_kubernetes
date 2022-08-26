import requests





password = "OeKbgKDYJgGnEnaKknED"
auth_url = 'http://a9cea8116617a43c59acc7f03669c088-1194859127.us-east-2.elb.amazonaws.com:8081/v1/auth'
auth_data = {"username":"demo-superuser","password":password}
y = requests.post(auth_url,json=auth_data,headers={"Content-Type":"application/json"})
print(y.text)
