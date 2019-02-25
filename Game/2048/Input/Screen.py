import numpy as np
import cv2
from PIL import ImageGrab as ig
import pytesseract
cv2.setUseOptimized(False)
icon = cv2.imread('/Users/Sami/Documents/Folder/Coding/Python/Machine-Learning/Mario Kart/I\O/Icon3.png',0)


def getInput():
    screen = ig.grab(bbox=(2000,330,2520,900))
    screen = np.asarray(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)


    return screen
def reward(screen):
    score = ig.grab(bbox=(2300,280,2400,320))
    score = np.asarray(score)
    score = cv2.cvtColor(score, cv2.COLOR_BGR2GRAY)
    print pytesseract.image_to_string(cv2.imread("/Users/Sami/Documents/Folder/Coding/Python/Machine-Learning/2048/Input/a.png"))
    return score
while(True):
    e1 = cv2.getTickCount()

    screen = getInput()
    score = reward(screen)

    cv2.imshow("test", np.asarray(score))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


    # NOTE: tick speed
    e2 = cv2.getTickCount()
    print (e2 - e1)/cv2.getTickFrequency()
