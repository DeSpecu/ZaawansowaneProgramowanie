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

(h, w) = image.shape[:2]
roi_width = 100

for x in range(0, w - roi_width, 10):
    roi = image[0:100, x:x+roi_width]
    cv2.imshow("Przesuwany", roi)
    if cv2.waitKey(100) == ord('q'):
        break

cv2.destroyAllWindows()