import requests

url = "http://127.0.0.1:5000/detect_upload"
files = {"file": open(r"sciezka", "rb")}

response = requests.post(url, files=files)

print(response.json())