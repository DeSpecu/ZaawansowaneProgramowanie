import cv2
import configparser
from imutils import resize

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Błąd podczas wczytywania pliku konfiguracyjnego: {e}")
    exit()

path = config['Paths']['image_path']

image = cv2.imread(path)

resized = resize(image, height=400)

cv2.imshow("Wysokosc 400", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()