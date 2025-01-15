import cv2
import pytesseract
import yaml

def Czytaj(sciezka):
    with open('config.yaml') as file:
        config = yaml.safe_load(file)

    img = cv2.imread(sciezka)

    pytesseract.pytesseract.tesseract_cmd = config["paths"]["tesseract_path"]

    print(pytesseract.image_to_string(img))

Czytaj(r"C:\Users\szymk\Desktop\OIP.jpg")