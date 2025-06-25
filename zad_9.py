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
image_copy[50:100, 50:100] = [0, 0, 0] #czarny, bo akurat na orazie białe tło

cv2.imshow("Przed zmianą", image)
cv2.imshow("Po zmianie", image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()