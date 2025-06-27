import cv2
import configparser
import numpy as np

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Błąd podczas wczytywania pliku konfiguracyjnego: {e}")
    exit()

path = config['Paths']['image_path']
image = cv2.imread(path)

height, width, _ = image.shape
right_half = image[:, width//2:]
flipped_part = cv2.flip(right_half, 1)

img_copy = image.copy()
img_copy[:, width//2:] = flipped_part

cv2.imshow("Częściowo odbity obraz", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()