# teleLogger
Captures and sends photo from webcam, IP and ISP details to your telegram account each time your computer is turned on.

## Want to know who used your PC when you were gone?
This program runs in background, starts up automatically on pc startup and captures a webcam photo and other details like IP address and ISP details. Location may not be accurate as it is from ISP and not GPS
Sends the captured information to your telegram account.
Saves the file locally and also logs it


# Requirements
- OpenCV
- python-telegram-bot
- Requests

# 1 min setup
- Launch init.py in Windows
- Enter your Telegram bot token when asked for.

Tested on Windows 10, Linux
init.py for Windows, Linux users won't need it

The to-do list:
- Face recognition 
- Trigger the script on Shutdown to record logoff details
