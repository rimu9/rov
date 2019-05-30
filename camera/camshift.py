import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#ret,frame = cap.read()
#print frame.shape
#cv2.imshow('img1',frame)
while True:
    ret, frame = cap.read()
    if ret is True:
        cv2.imshow("frame",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        box = cv2.selectROI(frame, False)
        (r,c,w,h) = [int(v) for v in box]
        track_window = (c,r,w,h)
        roi = frame[r:r+h, c:c+w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        #cv2.imshow('img2',hsv_roi)
        mask = cv2.inRange(hsv_roi, np.array((0.,44.,46.)), np.array((10.,255.,255.)))
        #cv2.imshow('img3',mask)
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1) #stop conditions---when stop
        break  
#track_window = (c,r,w,h)
#cv2.rectangle(frame,(c,r),(c+w,r+h),255,2)
#cv2.imshow("frame",frame)
#cv2.waitKey(0)
#roi = frame[r:r+h, c:c+w]
#hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#cv2.imshow('img2',hsv_roi)
#mask = cv2.inRange(hsv_roi, np.array((0.,44.,46.)), np.array((10.,255.,255.)))
#cv2.imshow('img3',mask)
#roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
#cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
#term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1) #stop conditions---when stop
while(True):
    ret, frame = cap.read()
 
    if ret is True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        #cv2.imshow('img3',dst)
        ret,track_window = cv2.CamShift(dst,track_window,term_crit)
        
        x,y,w,h = track_window
        cv2.rectangle(frame,(x,y),(x+w,y+h),255,2)
        cv2.rectangle(frame,(200,250),(300,350),255,2)
        cv2.imshow("frame",frame)
        
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
    else:
        break


cv2.destroyAllWindows()
cap.release()
