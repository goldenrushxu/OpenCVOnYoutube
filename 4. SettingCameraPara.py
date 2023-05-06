import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,100)
cap.set(4,100)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.line(gray, (100,100), (2000,2000),(255,0,0),10)

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + '  Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        gray = cv2.putText(gray,datet,(10,50),font,1,(255,0,0),1,cv2.LINE_AA)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 



cap.release()
cv2.destroyAllWindows()