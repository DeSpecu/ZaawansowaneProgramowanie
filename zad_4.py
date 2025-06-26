import cv2
import configparser
from imutils import translate

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

angle = float(input("Podaj kąt obrotu: "))
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Obrocony", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
