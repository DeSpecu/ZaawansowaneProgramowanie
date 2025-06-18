import cv2

image = cv2.imread(r"C:\Users\szymk\Downloads\pingwin.png")

cv2.namedWindow("Obraz", cv2.WINDOW_NORMAL)
cv2.imshow("Obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()