import cv2 as cv  # We have imported the package
import winsound
cam = cv.VideoCapture(0)   # we have allowed python to capture the video of our webcam
while cam.isOpened():
    tanmay,frame1 = cam.read()
    tanmay,frame2 = cam.read()
    diff = cv.absdiff(frame1,frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (9, 9), 0)
    tan,thresh =cv.threshold(blur, 25,260,cv.THRESH_BINARY)
    dilated = cv.dilate(thresh,None,iterations=3)
    countours,_ = cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(frame1,countours,-1,(0,255,0),2)
    for c in countours:
        if cv.contourArea(c) < 3000:
            continue
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(frame1,(x,y),(x+w, y+h),(0,255,0),3)
        winsound.Beep(1000,100)
    cv.imshow('Security Camera', frame1)


    if cv.waitKey(10) == ord('a'):
        break