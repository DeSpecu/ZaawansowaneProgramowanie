import cv2
import configparser
from imutils import rotate

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except configparser.Error as e:
    print(f"Błąd podczas wczytywania pliku konfiguracyjnego: {e}")
    exit()

path = config['Paths']['image_path']
image = cv2.imread(path)
h, w, _ = image.shape
center = (w // 2, h // 2)

result = image.copy()
for _ in range(3):
    M = cv2.getRotationMatrix2D(center, 30, 1.0)
    result = cv2.warpAffine(result, M, (w, h))

M90 = cv2.getRotationMatrix2D(center, 90, 1.0)
rot90 = cv2.warpAffine(image, M90, (w, h))

cv2.imshow("3x30", result)
cv2.imshow("1x90", rot90)
cv2.waitKey(0)
cv2.destroyAllWindows()