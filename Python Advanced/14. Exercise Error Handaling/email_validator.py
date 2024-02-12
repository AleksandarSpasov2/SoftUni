class NameTooShort(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ('com', 'bg', 'net', 'org')
MIN_NAME_SYMBOLS = 4


email = input()

while email != 'End':

    if len(email.split("@")[0]) <= MIN_NAME_SYMBOLS:
        raise NameTooShort(f"Name must be more than 4 characters")
    elif '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + n for n in VALID_DOMAINS)}")

    print("Email is valid")

    email = input()

