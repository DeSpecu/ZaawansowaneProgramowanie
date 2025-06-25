import cv2
import numpy as np

image = np.zeros((300, 300, 3), dtype=np.uint8)

center = (150, 150)

top_left = (center[0] - 50, center[1] - 50)
bottom_right = (center[0] + 50, center[1] + 50)

cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
cv2.circle(image, center, 30, (255, 0, 0), 2)

cv2.imshow("Kwadrat z okręgiem", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
