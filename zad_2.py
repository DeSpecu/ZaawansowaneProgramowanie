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
path2 = config['Paths']['image_path2']

image = cv2.imread(path)
image2 = cv2.imread(path2)

img1 = cv2.resize(image, (300, 300))
img2 = cv2.resize(image2, (300, 300))

diff = cv2.bitwise_xor(img1, img2)

cv2.imshow("Obraz 1", img1)
cv2.imshow("Obraz 2", img2)
cv2.imshow("Roznice", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()