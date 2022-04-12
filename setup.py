import os
import time
from time import sleep
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

print("Пожалуйста подождите..")
sleep(2)
print("\nУстановка...")
sleep(2)
os.system("pkg install git && pkg install python && pkg update && pkg upgrade && git clone https://github.com/KetoIT/telebot && cd telebot && pip install -r requirements.txt && python setup.py")
