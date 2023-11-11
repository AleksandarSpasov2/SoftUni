class Vehicle:

    def __int__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            return f"Successfully bought a {self.type}. Change: {owner}"
        self.owner = owner

        elif money < self.rpice:
        



