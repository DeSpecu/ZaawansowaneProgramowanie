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

# OpenCV
M = cv2.getRotationMatrix2D(center, 60, 1.0)
rot_cv2 = cv2.warpAffine(image, M, (w, h))

# imutils
rot_imutils = rotate(image, 60)

cv2.imshow("OpenCV warpAffine 60°", rot_cv2)
cv2.imshow("imutils.rotate 60°", rot_imutils)
cv2.waitKey(0)
cv2.destroyAllWindows()