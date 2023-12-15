import numpy as np
import cv2 as cv

class CMyImage():
    """
    Transformer class for image processing
    """
    def __init__(self, a_Image: np.ndarray | None = None):
        self.a_Image = a_Image
        self.l_Transformations = {
            ord('b'):False,
            ord('v'):False,
            ord('h'):False,
            ord('n'):False,
            ord('g'):False,
            ord('t'):False
        }

    def printTransformMenu(self):
        print("""b - blur
v - vertical flip
h - horizontal flip
n - RGB noise
g - grayscale
t - threshold
c - clear all
""")

    def setImage(self, a_Image: np.ndarray):
        """
        Set new image (frame)
        """
        self.a_Image = a_Image

    def getImage(self):
        """
        Get current image
        """
        return self.a_Image
    
    def getShape(self):
        """
        Get current image shape
        """
        if self.a_Image is not None:
            return self.a_Image.shape
    
    def grayscale(self):
        """
        Transform to grayscale (BGR format)
        """
        if self.a_Image is not None:
            self.a_Image = cv.cvtColor(cv.cvtColor(self.a_Image, cv.COLOR_BGR2GRAY),cv.COLOR_GRAY2BGR)
    
    def thresh(self):
        """
        Apply thresholding (BGR format)
        """
        if self.a_Image is not None:
            self.a_Image = cv.cvtColor(self.a_Image, cv.COLOR_BGR2GRAY)
            self.a_Image = cv.threshold(self.a_Image, 0, 255, cv.THRESH_OTSU)[1]
            self.a_Image = cv.cvtColor(self.a_Image,cv.COLOR_GRAY2BGR)

    def flip(self, iCode: int):
        """
        Flip image
        """
        if self.a_Image is not None:
            self.a_Image = cv.flip(self.a_Image, iCode)

    def blur(self):
        """
        Apply gaussian blur
        """
        if self.a_Image is not None:
            self.a_Image = cv.GaussianBlur(self.a_Image, (7,7), 3.0)

    def noise(self):
        """
        Apply noise
        """
        if self.a_Image is not None:
            a_Noise = np.round(np.random.random(self.a_Image.shape)*255).astype(np.uint8)
            self.a_Image = cv.addWeighted(
                self.a_Image, .75,
                a_Noise, .25,
                0.0
            )

    def toggleTransformation(self, s_Key: str):
        """
        Toggle transformation state variable
        """
        if s_Key in self.l_Transformations.keys():
            self.l_Transformations[s_Key] = not self.l_Transformations[s_Key]
        elif s_Key == ord('c'):
            for s_Key in self.l_Transformations:
                self.l_Transformations[s_Key] = False

    def transform(self):
        """
        Apply transformations
        """
        if self.l_Transformations[ord('h')]:
            self.flip(1)
        if self.l_Transformations[ord('v')]:
            self.flip(0)
        if self.l_Transformations[ord('n')]:
            self.noise()
        if self.l_Transformations[ord('b')]:
            self.blur()
        if self.l_Transformations[ord('g')]:
            self.grayscale()
        if self.l_Transformations[ord('t')]:
            self.thresh()
