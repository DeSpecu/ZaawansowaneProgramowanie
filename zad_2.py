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

flipped = cv2.flip(image, 0)

cv2.imshow("Oryginalny", image)
cv2.imshow("Odbicie", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()