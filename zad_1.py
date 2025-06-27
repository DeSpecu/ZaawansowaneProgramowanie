import cv2
import numpy as np

trojkkat = np.zeros((300, 300), dtype="uint8")
okrag = np.zeros((300, 300), dtype="uint8")

pts = np.array([[50, 250], [150, 50], [250, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(trojkkat, [pts], 255)

cv2.circle(okrag, (150, 150), 100, 255, -1)

and_example = cv2.bitwise_and(trojkkat, okrag)
or_example = cv2.bitwise_or(trojkkat, okrag)
xor_example = cv2.bitwise_xor(trojkkat, okrag)
not_example = cv2.bitwise_not(trojkkat)

cv2.imshow("Trojkat", trojkkat)
cv2.imshow("Okrag", okrag)
cv2.imshow("AND", and_example)
cv2.imshow("OR", or_example)
cv2.imshow("XOR", xor_example)
cv2.imshow("NOT Trojkat", not_example)
cv2.waitKey(0)
cv2.destroyAllWindows()