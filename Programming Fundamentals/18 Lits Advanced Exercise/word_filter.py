user_input = input().split()

even_words = [word for word in user_input if len(word) % 2 == 0]

print("\n".join(even_words))