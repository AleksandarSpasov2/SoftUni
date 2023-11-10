class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        first_letter_list = []
        for word in self.products:
            if word[0] == first_letter_list:
                first_letter_list.append(word)
        return first_letter_list

    def __repr__(self):
        return f'Items in the {self.name} catalogue:\n '

