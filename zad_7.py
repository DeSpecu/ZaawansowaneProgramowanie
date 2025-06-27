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

h,w,c = image.shape
h_step = h // 3
w_step = w // 3

for i in range(3):
    for j in range(3):
        part = image[i*h_step:(i+1)*h_step, j*w_step:(j+1)*w_step]
        cv2.imshow("Fragment", part)

cv2.waitKey(0)
cv2.destroyAllWindows()