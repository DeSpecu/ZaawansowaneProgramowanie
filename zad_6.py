import cv2
import configparser
from imutils import resize

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Błąd podczas wczytywania pliku konfiguracyjnego: {e}")
    exit()

path = config['Paths']['image_path']

image = cv2.imread(path)

flip_type = int(input("Wybierz typ odbicia (0=pionowe, 1=poziome, -1=obie osie): "))

if flip_type in [-1, 0, 1]:
    flipped = cv2.flip(image, flip_type)
    cv2.imshow("Wynik odbicia", flipped)
else:
    print("Nieprawidłowy wybór.")

cv2.waitKey(0)
cv2.destroyAllWindows()