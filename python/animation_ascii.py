import time
import os

fps = 10 

frames = ['''''']

while True:
    for frame in frames:
        os.system('cls')
        print(frame)
        time.sleep(1/fps)