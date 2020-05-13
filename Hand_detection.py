from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep
import cv2
import numpy as np
from selenium.webdriver.common.keys import Keys
import random

cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand.xml')
count = 0
print("ok")
driver = webdriver.Chrome(executable_path='/home/stsfaroz/chromedriver_linux64/chromedriver')
driver.get('https://chromedino.com/')


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2)
    contour = hands
    contour = np.array(contour)

    if count==0:

        if len(contour)==2:
            cv2.putText(img=frame, text='Started', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if count>0:

        if len(contour)>=2:
            cv2.putText(img=frame, text='.....', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(255, 0, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour)==1:
            cv2.putText(img=frame, text='Jump pannuda', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            driver.find_element_by_css_selector('body').send_keys(Keys.UP)
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour)==0:
            cv2.putText(img=frame, text='Odu Raja', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 0, 255))


    count+=1

    cv2.imshow('Play Game', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    


cap.release()
cv2.destroyAllWindows()
driver.quit()
