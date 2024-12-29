from typing import List, Optional
import requests
import argparse

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
            f"Longitude: {self.longtitude}\n"
            f"Latitude: {self.latitude}\n"
            f"Phone: {self.phone}\n"
            f"Website: {self.website_url}\n"
            )
    
    def fetch_breweries(city: Optional[str] = None):
        url = "https://api.openbrewerydb.org/breweries"
        params = {"per_page": 20}
        if city:
            params["by_city"] = city

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response


parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, help="Killeshin", required=False)
args = parser.parse_args()

odpowiedz = Brewery.fetch_breweries(city=args.city)

if odpowiedz.status_code == 200:
    dane = odpowiedz.json()
    for browar in dane:
        print(str(browar)+"\n")
else:
    print("Błąd")