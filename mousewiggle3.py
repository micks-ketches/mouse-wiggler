import os
import sys
import time
import math
import threading
import numpy as np

def autopyCheck():
    try:
         import autopy3
    except ImportError:
        print(
"""
to install autopy:
$ git clone git://github.com/Riamse/autopy3

$ cd autopy3

$ python3 setup.py build

$ python3 setup.py install
"""
            )
    else:
        global autopy
        autopy = __import__('autopy3', globals(), locals())


autopyCheck()
# Circle portion
width, height = 400, 400
a, b = 200, 200
r = 150

# Lemniscate portion
alpha = 200
instance = np.linspace(0, 2*np.pi, num=1000)
x = [(alpha * np.sqrt(2)*np.cos(i) / (np.sin(i)**2+1))+400 for i in instance]
y = [alpha * np.sqrt(2)*np.cos(i)*np.sin(i) / (np.sin(i)**2+1)+400 for i in instance]



timeInterval = input('Set interval (in seconds) between mouse movement: ')
timeInterval = int(timeInterval)

def stopCheck():
    endRun = input('You can stop this at any time by end ' + '\x1b[6;37;44m' + "end" + '\x1b[0m \n')
    if endRun == "end":
        os._exit(1)

def drawCicle():
    for x in range(0, 3):
        for angle in range(0, 360, 1):
            x = r * math.sin(math.radians(angle)) + a
            y = r * math.cos(math.radians(angle)) + b
            autopy.mouse.move(int(x),int(y))
            time.sleep(0.002)

def drawLemniscate():
    global x, y
    for n, m in zip(x, y):
        autopy.mouse.move(int(n), int(m))
        time.sleep(0.002)

def mouseMove():
    counter = 0
    while counter < 4:
        if (counter % 2 == 0):
            drawCicle()
        else:
            for x in range(0, 3):
                drawLemniscate()
        counter += 1
    else:
        print('Drawing circles')
        print(('moving once more in ' + str(timeInterval) + ' seconds...'))
        counter = 0
        time.sleep(timeInterval)
        mouseMove()

while True:
    daemon_mouseMove = threading.Thread(name='mouse', target=mouseMove)
    daemon_stopCheck = threading.Thread(name='stop', target=stopCheck)

    daemon_mouseMove.start()
    daemon_stopCheck.start()
    daemon_mouseMove.join()
    daemon_stopCheck.join()
