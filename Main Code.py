import pyautogui
import cv2
import numpy as np

resolution=pyautogui.size()#returns current screen resolution
codec=cv2.VideoWriter_fourcc(*"XVID")#converts a string(4 chars) to int
filename='Screen Recording.avi'#file name
fps=60#specific fps if we want
out=cv2.VideoWriter(filename,codec,fps,resolution)#To save a video in opencv..
cv2.namedWindow('LIVE',cv2.WINDOW_NORMAL)
cv2.resizeWindow('LIVE',480,270)
while True:
    image=pyautogui.screenshot()#takes screenshot
    frame=np.array(image)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('LIVE',frame)
    if cv2.waitKey(1)==ord('q'):#if u press 'q' recording will be stopped
        break
out.release()
cv2.destroyAllWindows()