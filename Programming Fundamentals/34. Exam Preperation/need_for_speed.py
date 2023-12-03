number_of_cars = int(input())
car_dict = {}
for cars in range(number_of_cars):
    user_input = input().split("|")
    car = user_input[0]
    mileage = int(user_input[1])
    fuel = int(user_input[2])
    car_dict[car] = {'mileage': 0, "fuel": 0}

