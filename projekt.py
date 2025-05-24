import cv2
import os
import xml.etree.ElementTree as ET
import time
from fast_alpr import ALPR
import yolov5
from fast_alpr.alpr import ALPR

SCIEZKA_ZDJECIA = r"Ścieżka do ustawienia"
XML_POPRAWNE_SCIEZKA = r"Śceiżka do ustawienia"
model = yolov5.load('keremberke/yolov5n-license-plate')
    
alpr = ALPR(
        detector_model="yolo-v9-t-256-license-plate-end2end",
        ocr_model="global-plates-mobile-vit-v2-model",
)

def znajdz_tablice(sciezka):
    obraz = cv2.imread(sciezka)

    tablica = model(obraz)
    odczyty = tablica.pred[0]
    max_obszar = 0
    najlepszy_kandydat = None
    if odczyty.shape[0] > 0:
        for odczyt in odczyty:
            x_min, y_min, x_max, y_max = map(int, odczyt[:4]) 

            if x_min < 0: 
                x_min = 0
            if y_min < 0: 
                y_min = 0
            if x_max > obraz.shape[1]: 
                x_max = obraz.shape[1] 
            if y_max > obraz.shape[0]: 
                y_max = obraz.shape[0] 

            if x_min < x_max and y_min < y_max:
                obszar = (x_max - x_min) * (y_max - y_min)
                if obszar > max_obszar:
                    max_obszar = obszar
                    najlepszy_kandydat = obraz[y_min:y_max, x_min:x_max]

    return najlepszy_kandydat

def ocr(obraz):
    try:
        alpr_dane = alpr.predict(obraz)
        ocr_dane = alpr_dane[0].ocr.text
        return ocr_dane
    
    except Exception as e:
        print(f"[OCR] Błąd: {e}")
        return "Błąd"
    
def process_image(obraz):
    nazwa = os.fsdecode(obraz)
    obraz = cv2.imread(os.path.join(f'{SCIEZKA_ZDJECIA}/plates', nazwa))
    tablica = ocr(obraz)
    return (nazwa, tablica)

if __name__ == '__main__':
    start = time.time()
    dict_dane_poprawne = {}
    dict_dane_odczytane = {}
    dane = ET.parse(XML_POPRAWNE_SCIEZKA).getroot()
    sciezka_zapis = f'{SCIEZKA_ZDJECIA}/plates'
    for child in dane.iter('image'):
        dict_dane_poprawne[child.get('name')] = child.find('box/attribute').text

    if not os.path.exists(sciezka_zapis):
        os.makedirs(sciezka_zapis)

        do_odczytania_tablic = [s for s in os.listdir(SCIEZKA_ZDJECIA) if s.endswith('.jpg')]

        for obraz in do_odczytania_tablic:
            print(f'Przetwarzanie {obraz}')
            nazwa = os.fsdecode(obraz)
            przeczytana = znajdz_tablice(os.path.join(SCIEZKA_ZDJECIA, nazwa))
            if przeczytana is None:
                continue
            else:
                cv2.imwrite(fr'{sciezka_zapis}/{nazwa}', przeczytana)

    images = [s for s in os.listdir(os.path.join(SCIEZKA_ZDJECIA, 'plates')) if s.endswith('.jpg')]
    
    for obraz in images:
        nazwa, tablica = process_image(obraz)
        dict_dane_odczytane[nazwa] = tablica

    ile = 0
    for x in dict_dane_odczytane:
        print(f'Odczytane dla {x} {dict_dane_odczytane[x]}, powinno być: {dict_dane_poprawne[x]}')
        if dict_dane_poprawne[x] == dict_dane_odczytane[x]:
            ile += 1

    print(f'Zgadza się {ile} z {len(dict_dane_poprawne)} Procentowo: {ile/len(dict_dane_poprawne)*100:.2f}%')
    stop = time.time()
    print(f'Zajęło to {stop - start:.2f} sekund')