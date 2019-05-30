from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import sys

if __name__ == '__main__' :
    
    #set up tracker
    tracker = cv2.TrackerCSRT_create()
    
    video = cv2.VideoCapture(0)
    ret,frame = video.read()
    if ret is not True:
        print ("open camera failed")
        sys.exit()
        
    initBB = None
    fps = None
    
    while True:
        ret,frame = video.read()
        
        if frame is None:
            print ("frame is none,read camera error")
        
        #process the video
        if initBB is not None:
            print ("init is not none")
            (sucess, box) = tracker.update(frame)
            timer = cv2.getTickCount()
            fps = 0.04*cv2.getTickFrequency() / (cv2.getTickCount() - timer)
            if sucess:
                (x,y,w,h) = [int(v) for v in box]
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2) 
                #fps.update()
                #fps.stop()
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("s"):
            initBB == cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
            OK = tracker.init(frame, initBB)
            #fps = FPS().start()
        elif key == ord("q"):
            break
    
    video.release()
    cv2.destroyAllWindows()
    