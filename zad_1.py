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

height, width = image.shape[:2]
center = (width // 2, height // 2)
bottom_right = (width - 1, height - 1)

cv2.line(image, center, bottom_right, (255, 0, 0), 2)

cv2.imshow("Linia", image)
cv2.waitKey(0)
cv2.destroyAllWindows()