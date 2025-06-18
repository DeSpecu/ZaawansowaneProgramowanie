import cv2

image_gray = cv2.imread(r"C:\Users\szymk\Downloads\pingwin.png", cv2.IMREAD_GRAYSCALE)
(h, w) = image_gray.shape[:2]
print(f"Liczba kanałów: 1")