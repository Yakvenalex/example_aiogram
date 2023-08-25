#!/home/ПАПКА_С_БОТОМ/env/bin/python3
import os
import subprocess

#Путь к скрипту aigram.py
script_path = os.path.join(os.path.dirname(__file__), '/home/ПАПКА_С_БОТОМ/aigram.py')

if os.path.exists(script_path):
    subprocess.run(['/home/ПАПКА_С_БОТОМ/env/bin/python3', script_path], check=True)
else:
    print("Не удалось найти скрипт aigram.py.")
