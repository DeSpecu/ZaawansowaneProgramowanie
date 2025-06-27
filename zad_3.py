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

h,w,c = image.shape

roi = image[0:, w//2:]

cv2.imshow("Połowa", roi)
cv2.waitKey(0)