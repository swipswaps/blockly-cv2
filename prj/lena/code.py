
import cv2
import numpy as np

image = None


image = cv2.imread('media/lena.jpg',1)cv2.imshow('mywin',image)
if cv2.waitKey(0)&0xff == 27:
  pass
cv2.destroyAllWindows()