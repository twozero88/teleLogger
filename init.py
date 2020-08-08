import os
import shutil
import requests
token = str(input("Enter your telegram token : "))
resp = requests.get('https://api.telegram.org/bot'+token+'/getUpdates')
print('Getting Chat ID...')
chatid = str(resp.json()['result'][0]['message']['chat']['id'])
with open('creds','w') as f:
	f.write(token+'\n'+chatid)
import t
print("Sending a test image....")
t.sendAnimation('setup.gif','Workingg!')
input('Proceed with next steps if you just got a message from your bot. Restart setup if not and Check your botToken and chatId')
if not os.path.exists('C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\launcher - Shortcut.lnk'):
	user = os.environ['USERPROFILE'].split("\\")[-1]
	src = os.getcwd()+"\\launcher - Shortcut.lnk"
	dest = "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\launcher - Shortcut.lnk"
	shutil.copyfile(src,dest)

print('--------------------Installing requirements--------------------')
os.system('pip install -r requirements.txt')
print('--------------------Done--------------------')
print('Running a test...')
os.system('python cap.py Testing')
# print('')
# print('')
# print('')
# print('----------------------------------------------------------------')
# input("You need to restart your computer to see it in work...Press enter after you save your unsaved work to restart.")
# input()
# os.system('shutdown /r /t 1')