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
center_pixel = image[center_y, center_x]
print(f"Środek obrazu: ({center_x}, {center_y}), kolor: R={center_pixel[2]}, G={center_pixel[1]}, B={center_pixel[0]}")
cv2.imshow("Piksel", image)
cv2.waitKey(0)
cv2.destroyAllWindows()