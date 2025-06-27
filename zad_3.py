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

numpy_dark = image - 80

opencv_dark = cv2.subtract(image, 80 * np.ones(image.shape, dtype='uint8'))

cv2.imshow("NumPy", numpy_dark)
cv2.imshow("OpenCV", opencv_dark)
cv2.waitKey(0)
cv2.destroyAllWindows()