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

B, G, R = cv2.split(image)

R = cv2.add(R, 30)
G = cv2.subtract(G, 20)
B = cv2.add(B, 10)

filtered = cv2.merge([B, G, R])

cv2.imshow("Instagram", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()