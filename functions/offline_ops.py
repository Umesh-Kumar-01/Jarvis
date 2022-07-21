import time

import pyautogui
import numpy as np
import cv2


def takeScreenShot():
    try:
        myScreenShot = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(myScreenShot), cv2.COLOR_RGB2BGR)
        cv2.imwrite("image1.png", image)
    except Exception as e:
        print(e)
        return False

    return True


def typeAnything(string):
    time.sleep(1)
    pyautogui.write(string)
