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

M = np.float32([[1, 0, width // 2 + 50], [0, 1, height // 2 + 50]])
shifted = cv2.warpAffine(image, M, (width, height))

cv2.imshow("Przesuniete", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()