import cv2

image_gray = cv2.imread(r"C:\Users\szymk\Downloads\pingwin.png", cv2.IMREAD_GRAYSCALE)

cv2.imwrite(r"C:\Users\szymk\Downloads\pingwin_gray.png", image_gray)