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

xStart = input("Podaj startowe X: ")
xEnd = input("Podaj końcowe X: ")
yStart = input("Podaj startowe Y: ")
yEnd = input("Podaj końcowe Y: ")

roi = image[int(yStart):int(yEnd), int(xStart):int(xEnd)]

cv2.imshow("User", roi)
cv2.waitKey(0)