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

methods = {
    "NEAREST": cv2.INTER_NEAREST,
    "LINEAR": cv2.INTER_LINEAR,
    "CUBIC": cv2.INTER_CUBIC,
    "LANCZOS4": cv2.INTER_LANCZOS4
}

for name, method in methods.items():
    upscaled = cv2.resize(image, None, fx=3, fy=3, interpolation=method)
    cv2.imshow(name, upscaled)

cv2.waitKey(0)
cv2.destroyAllWindows()