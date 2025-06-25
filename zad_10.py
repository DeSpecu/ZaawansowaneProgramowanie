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
height, width, _ = image.shape

pixel1 = image[50, 50]
pixel2 = image[200, 200]

diff = np.abs(pixel1.astype(int) - pixel2.astype(int))
print(f"Różnice R: {diff[2]}, G: {diff[1]}, B: {diff[0]}")