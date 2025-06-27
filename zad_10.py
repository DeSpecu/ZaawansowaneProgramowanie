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

resized = resize(image, width=800)
cv2.imwrite("resized.jpg", resized)