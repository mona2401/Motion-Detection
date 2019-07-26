import cv2
video=cv2.VideoCapture(0)
first_frame=None
a=1
while True:
    a=a+1
    check,frame=video.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_delta=cv2.threshold(delta_frame,100,255,cv2.THRESH_BINARY)[1]
    dilate=cv2.dilate(thresh_delta,None,iterations=3)
    contours, _ =cv2.findContours(dilate.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c)>5000: 
            (x, y, w, h) = cv2.boundingRect(c) 
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2) 
    cv2.imshow("frame",frame)
    cv2.imshow("Kunu",gray)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("thresh",thresh_delta)
    key=cv2.waitKey(1)
    if key==ord('k'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
