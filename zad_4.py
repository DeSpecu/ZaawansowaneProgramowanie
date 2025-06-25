import cv2
import cv2
import configparser

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Błąd podczas wczytywania pliku konfiguracyjnego: {e}")
    exit()

path = config['Paths']['image_path']

image_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

cv2.imwrite(r"C:\Users\szymk\Downloads\pingwin_gray.png", image_gray)