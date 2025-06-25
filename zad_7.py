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

third_height, third_width = height // 3, width // 3
center_crop = image[third_height:2*third_height, third_width:2*third_width]

cv2.imshow("Środkowy", center_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()