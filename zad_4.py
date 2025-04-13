import cv2
image = cv2.imread("mem.jpg")

xStart = input("Podaj startowe X")
xEnd = input("Podaj końcowe X")
yStart = input("Podaj startowe Y")
yEnd = input("Podaj końcowe Y")

roi = image[int(xStart):int(xEnd), int(yStart):int(yEnd)]

cv2.imshow("User", roi)
cv2.waitKey(0)