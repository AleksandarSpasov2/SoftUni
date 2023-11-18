def main():
    user_input = input()
    unique_force_user = {}
    while True:
        if user_input == "Lumpawaroo":
            break

        if "|" in user_input:
            force_side, force_user = user_input.split(" | ")
            force_function(unique_force_user, force_side, force_user)

        elif "->" in user_input:
            force_user, force_side = user_input.split(" -> ")


def force_function(unique_force_user, force_side, force_user):
    if force_side not in unique_force_user.keys() and force_user not in unique_force_user.values():
        unique_force_user[force_side] = [force_user]
    elif force_user not in unique_force_user.values():
        unique_force_user[force_side] += [force_user]
    elif force_user in unique_force_user.values():
        pass


def user_function(unique_force_user, force_side, force_user):
    if











