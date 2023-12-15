import cv2 as cv
import numpy as np
from CMyImage import CMyImage

class CCamera:
    """
    Camera class for webcam functionality
    """
    def __init__(self, i_Name: int = 0):
        print(f"Initializing camera {i_Name}")
        self.i_DeviceName = i_Name
        print(f"Trying to access camera {i_Name}...")
        self.CCamera = cv.VideoCapture(self.i_DeviceName, cv.CAP_DSHOW)
        if not self.CCamera.isOpened(): raise Exception("Cannot open camera")
        print(f"Camera {self.i_DeviceName} is ready!")
        self.c_Frame = CMyImage()

    def grabFrame(self):
        """
        Grab new frame from webcam
        """
        b_Res, a_Output = self.CCamera.read()
        if b_Res:
            self.c_Frame.setImage(np.array(a_Output, dtype=np.uint8))
        else: 
            self.c_Frame.setImage(np.zeros(self.t_Shape, dtype=np.uint8))
        return self.c_Frame.getImage()

    def displayInLoop(self, s_BreakKey: str ='q', i_TargetFps: int = 60):
        """
        Display webcam feed in a loop
        """
        s_Key = ''
        self.c_Frame.printTransformMenu()
        while True:
            self.grabFrame()
            self.c_Frame.toggleTransformation(s_Key)
            self.c_Frame.transform()
            cv.imshow("Output", self.c_Frame.getImage())
            s_Key = cv.waitKey(1000//i_TargetFps)
            if s_Key == ord(s_BreakKey):
                break

    def close(self):
        """
        Close camera
        """
        self.CCamera.release()
        print(f"Camera {self.i_DeviceName} was closed!")