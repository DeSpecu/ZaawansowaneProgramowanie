import cv2

image = cv2.imread(r"C:\Users\szymk\Downloads\pingwin.png")
image_gray = cv2.imread(r"C:\Users\szymk\Downloads\pingwin_gray.png")
cv2.imshow("Obraz", image)
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()