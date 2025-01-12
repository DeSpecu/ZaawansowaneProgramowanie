class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Property: Area: {self.area} m^2, Rooms: {self.rooms}, "
                f"Price: {self.price} PLN, Address: {self.address}")

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House: Area: {self.area} m^2, Rooms: {self.rooms}, "
                f"Price: {self.price} PLN, Address: {self.address}, Plot: {self.plot} m^2")

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Flat: Area: {self.area} m^2, Rooms: {self.rooms}, "
                f"Price: {self.price} PLN, Address: {self.address}, Floor: {self.floor}")

house = House(area=150, rooms=5, price=500000, address="Główna 10", plot=300)
flat = Flat(area=60, rooms=3, price=250000, address="Krzywa 45", floor=5)

print(house)
print(flat)
