import requests
import urllib.parse
import os

with open('creds','r') as f:
	data = f.read()

data = data.split('\n')
token = data[0].strip()
teleChatID = str(data[1]).strip()
def sendImage(fname,msg):
    files = {'photo': open(fname, 'rb')}
    status = requests.post('https://api.telegram.org/bot{}/sendPhoto?chat_id={}&disable_notification=false&caption={}'.format(token,teleChatID,urllib.parse.quote(msg)), files=files)
    # print(status.json())
    return status.json()['ok']

def sendAnimation(fname,msg):
    files = {'animation': open(fname, 'rb')}
    status = requests.post('https://api.telegram.org/bot{}/sendAnimation?chat_id={}&disable_notification=false&caption={}'.format(token,teleChatID,urllib.parse.quote(msg)), files=files)
    # print(status.json())
    return status.json()['ok']

