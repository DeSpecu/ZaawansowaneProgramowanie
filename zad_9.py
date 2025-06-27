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

for scale in range(100, 301, 20):
    fx = scale / 100.0
    resized = cv2.resize(image, None, fx=fx, fy=fx)
    cv2.imshow(f"{scale}%", resized)
    cv2.waitKey(500)

cv2.destroyAllWindows()