import cv2

image = cv2.imread(r"C:\Users\szymk\Downloads\pingwin.png")

(h, w, c) = image.shape[:3]
print(f"Liczba kanałów: {c}")