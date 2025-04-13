import cv2
image = cv2.imread("mem.jpg")

#cv2.imshow("Original", image)

roi = image[0:100, 0:100]

cv2.imshow("100x100", roi)
cv2.waitKey(0)