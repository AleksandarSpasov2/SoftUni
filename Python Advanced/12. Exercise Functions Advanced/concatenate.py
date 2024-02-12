def concatenate(*args, **kwargs):
    new_string = ''.join(args)
    for key, value in kwargs.items():
        new_string = new_string.replace(key, value)

    return new_string




print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))