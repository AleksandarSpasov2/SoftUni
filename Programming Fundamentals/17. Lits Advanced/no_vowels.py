user_input = input()

vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]

user_input_without_vowels = [letter for letter in user_input if letter not in vowels]

print("".join(user_input_without_vowels))