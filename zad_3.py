import cv2
import configparser

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Błąd podczas wczytywania pliku konfiguracyjnego: {e}")
    exit()

path = config['Paths']['image_path']
image = cv2.imread(path)
resized = cv2.resize(image, (200, 300))

cv2.imshow("200x300", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()