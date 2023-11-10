class Catalogue:
    def __init__(self, name):
        self.first_letter_list = None
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        self.first_letter_list = []
        for word in self.products:
            if word[0] == self.first_letter_list:
                self.first_letter_list.append(word)
        return self.first_letter_list

    def __repr__(self):
        sorted_list = sorted(self.first_letter_list, key=lambda x: x.lower())
        return f'Items in the {self.name} catalogue:\n' \
               f'{sorted_list}'


