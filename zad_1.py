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

numpy_added = image + 50

opencv_added = cv2.add(image, 50 * np.ones(image.shape, dtype='uint8'))

cv2.imshow("Oryginalny", image)
cv2.imshow("NumPy", numpy_added)
cv2.imshow("OpenCV", opencv_added)
cv2.waitKey(0)
cv2.destroyAllWindows()