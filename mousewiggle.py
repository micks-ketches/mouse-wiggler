import autopy
import time
import math
width, height = 200, 200
a, b = 200, 200
r = 150
# to install autopy:
# $ git clone git://github.com/msanders/autopy.git
#
# $ cd autopy
#
# $ python setup.py build
#
# $ python setup.py install

timeInterval = raw_input('Set interval (in seconds) between mouse movement')

timeInterval = int(timeInterval)
timeInterval()
def drawCicle():
    for x in range(0, 3):
        for angle in range(0, 360, 1):
            x = r * math.sin(math.radians(angle)) + a
            y = r * math.cos(math.radians(angle)) + b
            autopy.mouse.move(int(x),int(y))
            time.sleep(0.002)
def mouseMove():
    counter = 1
    while counter < 4:
        drawCicle()
        counter += 1
    else:
        print('triggered')
        print('moving once more ')
        counter = 1
        time.sleep(timeInterval())
        mouseMove()

if __name__ == "__main__":
    mouseMove()
