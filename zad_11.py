import cv2
import numpy as np
import configparser

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Błąd podczas wczytywania pliku konfiguracyjnego: {e}")
    exit()

path = config['Paths']['image_path']

image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray)
brightest = image[maxLoc[1], maxLoc[0]]
print(f"Najjaśniejszy piksel: {maxLoc}, kolor: R={brightest[2]}, G={brightest[1]}, B={brightest[0]}")