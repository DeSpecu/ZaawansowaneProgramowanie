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
height, width, _ = image.shape

image_copy = image.copy()
half_height, half_width = height // 2, width // 2
image_copy[0:half_height, 0:half_width] = [255, 0, 0]  # Niebieski

cv2.imshow("Niebiesko", image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()