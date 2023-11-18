def main():
    unique_force_user = {}
    while True:
        user_input = input()
        if user_input == "Lumpawaroo":
            break

        if "|" in user_input:
            force_side, force_user = user_input.split(" | ")
            force_function(unique_force_user, force_side, force_user)

        elif "->" in user_input:
            force_user, force_side = user_input.split(" -> ")
            user_function(unique_force_user, force_side, force_user)

    print_function(unique_force_user)


def force_function(unique_force_user, force_side, force_user):
    if force_side not in unique_force_user.keys():
        unique_force_user[force_side] = []
    user_exists = False
    for user in unique_force_user.values():
        if force_user in user:
            user_exists = True
            break
    if not user_exists:
        unique_force_user[force_side].append(force_user)


def user_function(unique_force_user, force_side, force_user):
    for side, users in unique_force_user.items():
        if force_user in users:
            users.remove(force_user)
            break
        if force_side not in unique_force_user:
            unique_force_user[force_side] = []
        unique_force_user[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")


def print_function(unique_force_user):
    for force_side, force_users_list in unique_force_user.items():
        if force_users_list:
            print(f"Side: {force_side}, Members: {len(force_users_list)}")
            for user in force_users_list:
                print(f"! {user}")

main()









