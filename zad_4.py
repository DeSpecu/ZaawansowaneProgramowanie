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
height, width, _ = image.shape

shifted = translate(image, 100, 50)

cv2.imshow("Przesuniete", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()