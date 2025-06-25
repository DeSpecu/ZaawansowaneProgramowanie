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

pixel = image[0, 0]
b, g, r = pixel
print(f"Wartości piksela (0,0): R={r}, G={g}, B={b}")
