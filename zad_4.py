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

x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

if 0 <= x < width and 0 <= y < height:
    image[y, x] = [0, 0, 0]
    print(f"Piksel ustawiony na czarny")
else:
    print("Nieprawidłowe współrzędne")

cv2.imshow("Piksel", image)
cv2.waitKey(0)
cv2.destroyAllWindows()