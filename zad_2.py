import cv2
image = cv2.imread("mem.jpg")

h,w,c = image.shape

roi = image[h//2:, 0:]

cv2.imshow("Połowa", roi)
cv2.waitKey(0)