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
center_x = width // 2
center_y = height // 2

image_copy = image.copy()
start_x = center_x - 50
start_y = center_y - 50
image_copy[start_y:start_y + 100, start_x:start_x + 100] = [0, 0, 255]

cv2.imshow("Czerwono", image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()