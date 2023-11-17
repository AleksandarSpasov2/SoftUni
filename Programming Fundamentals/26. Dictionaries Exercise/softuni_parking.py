def main():
    registry = {}
    n = int(input())
    for _ in range(n):
        command = input().split()
        if command[0] == "register":
            username = command[1]
            license_plate = command[2]
            register_command(registry, username, license_plate)
        elif command[0] == "unregister":
            username = command[1]
            unregister_command(registry, username)

    print_function(registry)


def register_command(registry, username, license_plate):
    if username in registry.keys():
        print(f'ERROR: already registered with plate number {license_plate}')
    else:
        registry[username] = license_plate
        print(f"{username} registered {license_plate} successfully")


def unregister_command(registry, username):
    if username not in registry.keys():
        print(f"ERROR: user {username} not found")
    else:
        registry.pop(username)
        print(f"{username} unregistered successfully")


def print_function(registry):
    for key, value in registry.items():
        print(f'{key} => {value}')


main()