import subprocess
import time

subprocess.call(["python3", "_pick_place.py"])

while True:
    subprocess.call(["python3", "_demo.py"])
    time.sleep(1)