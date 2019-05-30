import cv2
import numpy
import time


#class CaptureManager(object):
    #def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = Flase):


    #@property
    #def channer(self):


    #@channer.setter
    #def channer(self, value):


    #@property
    #def frame(self):


    #@property
    #def isWritingImage(self):


    #@property
    #def isWritingVideo(self):


    #def enterFrame(self):


    #def exitFrame(self):



class WindowManager(object):
    def __init__(self, windowName, keypressCallback = None):
        self.keypressCallback = keypressCallback
        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True

    def show(self, frame):
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False
 
    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            keycode &= 0xFF
            self.keypressCallback(keycode)

