import requests
import json
#url = 'http://localhost:8080/users'
#data =  json.dumps({"name": "Ana","email": "Ana@gmail.com"})
headers = {'Content-Type': 'application/json'}

def postUsers(url, data):
    r = requests.post(url, data = data, headers = headers)
    print(r.content)

def postSurvey(url, data):   
    r = requests.post(url, data = data, headers = headers)
    print(r.content)

def getSurvey(url):
    r = requests.get(url)
    return r.json()

def sendEmail():
    url = 'http://localhost:8080/sendMail'
    headers = {'Content-Type': 'application/json'}
    data =  json.dumps({"email": "Ana@gmail.com", "survey_id": "6d2af7df-ea9c-4aff-b75d-8551506fe6b2"})
    r = requests.post(url, headers = headers, data = data )

    return r.json()

print(sendEmail())


