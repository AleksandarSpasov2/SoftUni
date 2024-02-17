def cookbook(*args):
    book = {}

    for recipe_name, cuisine, ingredients in args:
        if cuisine not in book:
            book[cuisine] = []
        book[cuisine].append({"name": recipe_name, "ingredients": ingredients})

    sorted_cuisines = sorted(book.keys(), key=lambda x: (-len(book[x]), x))

    result = ''
    for cuisine in sorted_cuisines:
        result += f'{cuisine} cuisine contains {len(book[cuisine])} recipes:\n'
        for recipe in sorted(book[cuisine], key=lambda x: x['name']):
            result += f'  * {recipe["name"]} -> Ingredients: {", ".join(recipe["ingredients"])}\n'

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))