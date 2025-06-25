import cv2
import numpy as np
import configparser

image = np.zeros((400, 400, 3), dtype=np.uint8)

cv2.rectangle(image, (0, 0), (100, 50), (0, 255, 0), -1)
cv2.rectangle(image, (300, 350), (399, 399), (0, 0, 255), 3)

cv2.imshow("Prostokąty", image)
cv2.waitKey(0)
cv2.destroyAllWindows()