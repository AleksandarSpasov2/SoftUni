class Vehicle:
    owner = None

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money: int, owner: str):
        if money >= self.price and Vehicle.owner is None:
            Vehicle.owner = owner
            return f"Successfully bought a {self.type}. Change: {owner}"

        elif money < self.price:
            return f"Sorry, not enough money"
        elif Vehicle.owner is not None:
            return f"Car already sold"

    def sell(self):
        if Vehicle.owner is not None:
            Vehicle.owner = None
        else:
            return f"Vehicle has no owner"

    def __repr__(self):
        if Vehicle.owner is not None:
            return f"{self.model} {self.type} is owned by: {Vehicle.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)






