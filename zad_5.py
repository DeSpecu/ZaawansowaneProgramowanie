import cv2
import numpy as np

image = np.zeros((400, 400, 3), dtype=np.uint8)
center = (200, 200)

for i in range(20, 121, 20):
    top_left = (center[0] - i//2, center[1] - i//2)
    bottom_right = (center[0] + i//2, center[1] + i//2)
    cv2.rectangle(image, top_left, bottom_right, (255, 255, 0), 1)

cv2.imshow("Kwadraty", image)
cv2.waitKey(0)
cv2.destroyAllWindows()