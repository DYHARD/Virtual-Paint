import cv2
# print("Yoo")
import numpy as np
url = "http://10.196.4.244:8080/video"
cap = cv2.VideoCapture(0)
#width id number 3
cap.set(3,640)
#length id number 4
cap.set(4,480)
#for brightness
cap.set(10,300)

colors=[[169,179,94,141,0,255]]
mycolor=[[]]
mypoints = []

def getContour(img):
    x,y,w,h=0,0,0,0
    contours, heirchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgResult,cnt,-1,(0,255,255),2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
            print(x,y,w,h)
    return ((x+w)//2),y
def drawOnCanvas(mypoints):
        for point in mypoints:
            cv2.circle(imgResult, (point[0], point[1]), 5, (0, 0, 255), cv2.FILLED)

def findColor(img,colors):
    newPoints=[]
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([colors[0][0], colors[0][2], colors[0][4]])
    upper = np.array([colors[0][1], colors[0][3], colors[0][5]])
    mask = cv2.inRange(imgHsv, lower, upper)
    x,y=getContour(mask)
    cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
    if x!=0 and y!=0:
        newPoints.append(([x,y]))
    return newPoints
    # imgResult = cv2.bitwise_and(img, img, mask=mask)
    # return imgResult

while True:
    success, img = cap.read()
    img = cv2.resize(img,(500,500))
    imgResult = img.copy()
    newPoints = findColor(img,colors)
    if len(newPoints)!=0:
        for p in newPoints:
            mypoints.append(p)
    if len(mypoints)!=0:
        drawOnCanvas(mypoints)
    cv2.imshow("result",imgResult)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break