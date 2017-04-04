# import the necessary packages
import numpy as np 
import cv2 

class ColorDescriptor:
    """
    Computes 3D HSV color histograms for different regions of the image. Simulates locality in the color dist.  

    """
    def __init__(self,bins):
        self.bins = bins

    def describe(self,image):
        """ Convert the image to HSV color space and initialize features 
        used to quantify image"""
        image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        features =[]

        """ Grab the dimensions and compute the center of the image """
        (h,w) = image.shape[:2]
        (cX, cY) = (int(w*0.5),int(h*0.5))

        """ Divide the image into four rectangles """
        segments = [(0,cX,0,cY),(cX,w,0,cY),(cX,w,cY,h),(0,cX,cY,h)]

        """ Construct an elliptical mask representing the center of the image """
        (axesX,axesY) = (int(w*0.75)/2,int(h*0.75)/2)
        ellipMask = np.zeros(image.shape[:2],dtype='uint8')
        cv2.ellipse(ellipMask,(cX,cY),(axesX,axesY),0,0,360,255,-1)

        """ Loop over segments """
        for (startX, endX, startY, endY) in segments:
            """ Construct a mask for each corner of the image, subtracting the elliptical center from it """
            cornerMask = np.zeros(image.shape[:2],dtype="uint8")
            cv2.rectangle(cornerMask,(startX,startY),(endX, endY), 255, -1)
            cornerMask = cv2.subtract(cornerMask, ellipMask)

            """ Extract color histogram from the image and update feature vector """
            hist = self.histogram(image, cornerMask)
            features.extend(hist)

        hist = self.histogram(image, ellipMask)
        features.extend(hist)

        return features

    def histogram(self, image, mask):
        # extract a 3D color histogram from the masked region of the
        # image, using the supplied number of bins per channel; then
        # normalize the histogram
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
            [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist,hist).flatten()

        # return the histogram
        return hist









