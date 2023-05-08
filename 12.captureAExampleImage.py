# tasks to do
# V 1. display menu
# V 1.1 use + and - to adjust sensitivity
# V don't need to 2. reduce display FPS, to increase response
# 3. locate base points, trim images according to base points
# 4. rotate images according to base points
# 5. stop auto focusing




import cv2
import datetime

img1 = cv2.imread('example.jpg')            #read example image
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('original',cv2.WINDOW_NORMAL)
cv2.resizeWindow('original',1600,900)
cv2.imshow('original',img1)       #show what's been read

# ==========================================
# show live video
cap = cv2.VideoCapture(1)       #select the second camera
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0)
cap.set(cv2.CAP_PROP_EXPOSURE,0.2)
                                #the arguement could be a file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
Sens = 100          #default sensitivity
font = cv2.FONT_HERSHEY_SIMPLEX
menu1 = "Press [E] to save example image"
menu2 = "Press [S] to save example image"
menu3 = "Press [+] or [-] to change sensitivity"
menu4 = "Press [Q] to quite"
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame',1600,900)

while (cap.isOpened()):
    ret, frame = cap.read()     #read camera

    # if cv2.waitKey(10) & 0xFF == ord('+') : #increase the sensitivity
    #     if Sens > 20:
    #         Sens = Sens - 20

    # if cv2.waitKey(10) & 0xFF == ord('-') : #reduce the sensitivity
    #     if Sens < 181:
    #         Sens = Sens + 20

    if cv2.waitKey(10) & 0xFF == ord('+') : #increase the sensitivity
        if Sens > 20:
            Sens = Sens - 20

    if cv2.waitKey(10) & 0xFF == ord('-') : #reduce the sensitivity
        if Sens < 181:
            Sens = Sens + 20
        
    # if (cv2.waitKey(10) & 0xFF == ord('s')) | (cv2.waitKey(10) & 0xFF == ord('S')):       #save current image when 'S'is pressed
    #     imgname = datet.replace(":"," ").replace("-"," ").replace("."," ") + '.jpg'
    #     cv2.imwrite(imgname , frame)      #save current picture into file

    if ret == True:

        if (cv2.waitKey(10) & 0xFF == ord('e')) | (cv2.waitKey(10) & 0xFF == ord('E')): #save example when 'E' is pressed
            cv2.imwrite('example.jpg', frame)      #save current picture into file
            img1 = cv2.imread('example.jpg')            #read example image
            gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            cv2.namedWindow('original',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('original',1600,900)
            cv2.imshow('original',img1)       #show what's been read

        gray2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # Calculate the absolute difference between the two images
        diff = cv2.absdiff(gray1, gray2)

        # Apply a threshold to the difference image
        thresh = cv2.threshold(diff, Sens, 255, cv2.THRESH_BINARY)[1]

        # Find the contours of the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw rectangles around the contours of the differences
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w>10:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        datet = str(datetime.datetime.now())
        sens_str = "Sensitivity: " + str((200-Sens)/20)

        frame = cv2.putText(frame,datet,(10,50),font,1,(255,0,0),1,cv2.LINE_AA)
        frame = cv2.putText(frame,menu1,(10,90),font,1,(255,0,0),1,cv2.LINE_AA)
        frame = cv2.putText(frame,menu2,(10,130),font,1,(255,0,0),1,cv2.LINE_AA)
        frame = cv2.putText(frame,menu3,(10,170),font,1,(255,0,0),1,cv2.LINE_AA)
        frame = cv2.putText(frame,menu4,(10,210),font,1,(255,0,0),1,cv2.LINE_AA)
        frame = cv2.putText(frame,sens_str,(10,250),font,1,(255,0,0),1,cv2.LINE_AA)

        cv2.imshow('frame',frame)       #show what's been read

        if (cv2.waitKey(10) & 0xFF == ord('q')) | (cv2.waitKey(10) & 0xFF == ord('Q')) :       #quit when 'q'is pressed
            imgname = datet.replace(":"," ").replace("-"," ").replace("."," ") + '.jpg'
            cv2.imwrite(imgname, frame)      #save current picture into file
            break

        if (cv2.waitKey(10) & 0xFF == ord('s')) | (cv2.waitKey(10) & 0xFF == ord('S')):       #save current image when 'S'is pressed
            imgname = datet.replace(":"," ").replace("-"," ").replace("."," ") + '.jpg'
            cv2.imwrite(imgname , frame)      #save current picture into file
    else:
        break

cap.release()
cv2.destroyAllWindows()
