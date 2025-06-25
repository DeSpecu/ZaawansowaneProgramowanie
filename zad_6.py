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

left_eye = (190, 110)
right_eye = (300, 110)
mouth = (240, 140)
face_center = (230, 130)

cv2.circle(image, left_eye, 40, (0, 0, 255), -1)
cv2.circle(image, right_eye, 40, (0, 0, 255), -1)
cv2.rectangle(image, (mouth[0] - 40, mouth[1] - 10), (mouth[0] + 40, mouth[1] + 10), (0, 255, 0), -1)
cv2.circle(image, face_center, 140, (255, 0, 0), 2)

cv2.imshow("Zamazanie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()