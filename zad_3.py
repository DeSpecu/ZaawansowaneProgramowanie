import cv2
image = cv2.imread("mem.jpg")

h,w,c = image.shape

roi = image[0:, w//2:]

cv2.imshow("Połowa", roi)
cv2.waitKey(0)