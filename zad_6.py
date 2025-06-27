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

fragment = image[50:150, 50:150] 
image[200:300, 200:300] = fragment 

cv2.imshow("Po wklejeniu", image)
cv2.waitKey(0)
cv2.destroyAllWindows()