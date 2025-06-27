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

resized = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)

cv2.imshow("Zmniejszenie", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()