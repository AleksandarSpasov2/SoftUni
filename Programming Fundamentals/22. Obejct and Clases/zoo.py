class Zoo:
    __animals = 0

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
        Zoo.__animals += 1

    def get_info(self, species):
        return f"{self.species} in {self.name}: {self.names}\nTotal animals: {self._animals}"


zoo_name = input()
zoo_object = Zoo(zoo_name)
n = int(input())
for animal in range(n):
    species, name = input().split()
    zoo_object.add_animal(species, name)

searched_species = input()
print(zoo_object.get_info(zoo_object))




