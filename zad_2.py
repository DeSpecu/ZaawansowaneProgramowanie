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

image_copy = image.copy()
height, width, _ = image.shape
image_copy[height - 1, width - 1] = [0, 0, 255] 

cv2.imshow("Przed zmianą", image)
cv2.imshow("Po zmianie", image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
