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
cubic = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
lanczos = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("Cubic", cubic)
cv2.imshow("Lanczos", lanczos)
cv2.waitKey(0)
cv2.destroyAllWindows()