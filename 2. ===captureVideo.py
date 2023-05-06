# can't get expected avi file output, apart from that, everything else is OK
# link for the video is:
# https://www.youtube.com/watch?v=-RtVZsCvXAQ&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=5 

import cv2

cap = cv2.VideoCapture(0)       #select the first camera
                                #the arguement could be a file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20, (640,480))
#output file, compression format, frames/second, resolution

# while(cap.isOpend()):         #if it's the wrong file or camera, while loop won't execute
print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()     #read camera
    if ret == True:

        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write(frame)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)       #show what's been read

        if cv2.waitKey(1) & 0xFF == ord('q'):       #quit when 'q'is pressed
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()