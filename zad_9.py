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

cropped = image[0:300, 0:300]
cv2.imwrite("cropped.jpg", cropped)

cv2.imshow("Przyciety", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()