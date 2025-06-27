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
half = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))

cv2.imshow("Pomniejszony", half)
cv2.waitKey(0)
cv2.destroyAllWindows()