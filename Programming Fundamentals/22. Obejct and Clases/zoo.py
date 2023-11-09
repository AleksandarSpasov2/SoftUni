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
        result = ''
        if species == "mammal":
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif species == "fish":
            result += f'Fishes in {self.name}: {", ".join(self.fishes)}\n'
        elif species == "fish":
            result += f'Birds in {self.name}: {", ".join(self.birds)}\n'

        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
zoo_info = Zoo(zoo_name)
n = int(input())
for animal in range(n):
    species, name = input().split()
    zoo_info.add_animal(species, name)
info = input()
print(zoo_info.get_info(info))




