import cv2
import time 
import numpy as np 


frame = cv2.resize(frame,(640,480))
image = cv2.resize(frame,(640,480))

cap=cv2.videoCpture(0)

time.sleep(2)
bg=0
for i in range(60):
    ret,bg= cap.read()
bg=np.flip(bg,axis=1)


while (cap.isOpened()):
    ret,img=cap.read()      
    if not ret :
        break
    img=np.flip(bg,axis=1)

    frame=cv2.cvtcolor(img,cv2.COLOR_BGR2HSV)
    f= frame - res
    f= np.where(f ==0,image,f)
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
   

    mask=cv2.inRange(frame,u_black, l_black) 
    res_1=cv2.bitwise_and(frame,frame,mask=mask)
     


   
    cv2.imshow("magic")
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()

     


