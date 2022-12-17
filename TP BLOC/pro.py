import cv2 as cv
import numpy as np
from  PIL import Image
import math

img = cv.imread('image072.png')
img = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
Y, Cr, Cb = cv.split(img)
cv.imshow("Y", Y)
cv.waitKey(0)