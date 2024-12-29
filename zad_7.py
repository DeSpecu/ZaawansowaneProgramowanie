import requests

class Brewery:
    def __init__(self,id,name, brewery_type, address_1, address_2,address_3, city, state_province,
                 postal_code, country, longtitude, latitude, phone, website_url, state, street):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longtitude = longtitude
        self.latitude  = latitude
        self.phone = phone
        self.website_url = website_url
        self.street = street
        self.state = state

    def __str__(self):
        return (
            f"Brewery ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"Street: {self.street}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Postal Code: {self.postal_code}\n"
            f"Country: {self.country}\n"
            f"Longitude: {self.longitude}\n"
            f"Latitude: {self.latitude}\n"
            f"Phone: {self.phone}\n"
            f"Website: {self.website_url}\n"
            )
    

url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

odpowiedz = requests.get(url)

if odpowiedz.status_code == 200:
    dane = odpowiedz.json()
    for browar in dane:
        print(str(browar)+"\n")
else:
    print("Błąd")
