class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address}, plot={self.plot}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: area={self.area}, rooms={self.rooms}, price={self.price}, address={self.address}, floor={self.floor}"


house = House(120, 5, 500000, "Warszawa, ul. Kwiatowa 1", 300)
flat = Flat(60, 3, 300000, "Krakow, ul. Kwiatowa 2", 4)

print(house)
print(flat)
