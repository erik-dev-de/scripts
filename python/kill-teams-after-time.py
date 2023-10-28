import psutil
import time

PROCNAME = "Teams.exe"

timeout_value = input("Insert time (in minutes):")

timeout_value = int(timeout_value) * 60

time.sleep(timeout_value) 

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()