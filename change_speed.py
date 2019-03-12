import numpy as np
import cv2
import time
###########################################
####Global Parameter                   ####
G_VideoCapFrom0 = cv2.VideoCapture('rgb_zhuanpan.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output3.avi',fourcc,5.0, (720,1280))

###########################################
####Sub Function                       ####
def F_PlayVideoUntilPressQ():
        while(G_VideoCapFrom0.isOpened()):
            ret, frame = G_VideoCapFrom0.read()
            if ret==True:
                frame=cv2.flip(frame, 1, dst=None)
                out.write(frame)

            else:
            #judge : can not load video or finished play
            #either can cause error:error: (-215) scn == 3 || scn == 4 in function cv::cvtColor
                print("can not load video or finished play")
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
###########################################
####Main Function                      ####
F_PlayVideoUntilPressQ()
G_VideoCapFrom0.release()
cv2.destroyAllWindows()