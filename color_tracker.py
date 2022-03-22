import cv2
import numpy as np
cap = cv2.VideoCapture(0)
def NULL(a):
    pass
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,240)
cv2.createTrackbar("H min","TrackBar",17,179,NULL)
cv2.createTrackbar("H max","TrackBar",125,179,NULL)
cv2.createTrackbar("S min","TrackBar",10,255,NULL)
cv2.createTrackbar("S max","TrackBar",98,255,NULL)
cv2.createTrackbar("V min","TrackBar",111,255,NULL)
cv2.createTrackbar("V max","TrackBar",255,255,NULL)
while True:
    success, img = cap.read()
    cv2.imshow("vdo", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("H min","TrackBar")
    h_max = cv2.getTrackbarPos("H max", "TrackBar")
    s_min = cv2.getTrackbarPos("S min", "TrackBar")
    s_max = cv2.getTrackbarPos("S max", "TrackBar")
    v_min = cv2.getTrackbarPos("V min", "TrackBar")
    v_max = cv2.getTrackbarPos("V max", "TrackBar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    # print(lower,upper)
    # cv2.waitKey(3)
    mask = cv2.inRange(imgHsv,lower,upper)
    imgResult = cv2.bitwise_not(img,img,mask=mask)
    #print("i",mask)
    cv2.imshow("HSV",imgHsv)
    cv2.imshow("mask",mask)
    cv2.imshow("color_detected",imgResult)
    cv2.waitKey(1)
