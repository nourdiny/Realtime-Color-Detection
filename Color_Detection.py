import cv2
import numpy as np



#########################
wImg = 350
hImg = 350
cap = cv2.VideoCapture(1)
cap.set(3,wImg)
cap.set(4,hImg)
###########################
def empty(a):
    pass
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)
nou = False
while True:
    if nou :
        susse, img = cap.read()
    else:
        img = cv2.imread("img/img3.png")

    img = cv2.resize(img , (wImg,hImg))
    imgHsv = cv2.cvtColor(img ,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    lowre = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lowre,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

    hstack = np.hstack([img,mask,result])


    #cv2.imshow("img",img)
    #cv2.imshow("imgHsv",imgHsv)
    #cv2.imshow("mask",mask)
    #cv2.imshow("result",result)
    cv2.imshow("vstack",hstack)
    if cv2.waitKey(1) & 0xFF == ord('n'):
        break
