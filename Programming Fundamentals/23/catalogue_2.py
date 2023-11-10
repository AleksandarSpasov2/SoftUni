class Catalogue:

    def __init__(self, name: str):
        self.first_letter_list = None
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        self.first_letter_list = [word for word in self.products if word.startswith(first_letter)]
        return self.first_letter_list

    def __repr__(self):
        items = "\n".join(s for s in self.first_letter_list)
        return f'"Items in the {self.name} catalogue:{items}'

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
