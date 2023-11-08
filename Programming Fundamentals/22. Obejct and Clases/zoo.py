class Zoo:
    _animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)

    def get_info(self, species):
        return f"{self.species} in {self.name}: {self.names}\nTotal animals: {self._animals}"
    

