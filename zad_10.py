import cv2
import configparser
from imutils import rotate

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Błąd podczas wczytywania pliku konfiguracyjnego: {e}")
    exit()

path = config['Paths']['image_path']
image = cv2.imread(path)
h, w, _ = image.shape
center = (w // 2, h // 2)

for angle in range(0, 361, 15):
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow(f"Obrót {angle}°", rotated)
    cv2.waitKey(500)

cv2.destroyAllWindows()