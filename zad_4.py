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

flipped_h = cv2.flip(image, 1)
flipped_v = cv2.flip(image, 0)
flipped_both = cv2.flip(image, -1)

cv2.imshow("Oryginał", image)
cv2.imshow("Poziome", flipped_h)
cv2.imshow("Pionowe", flipped_v)
cv2.imshow("Obie osie", flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()