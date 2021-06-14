my_list = list(input("Введите значения"))

for i in range(1, len(my_list), 2):
    my_list[i - 1 ], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)

while True:
    user_month = input("Введите номер месяца")
    if user_month.isdigit() and 1 <= int(user_month) <= 12:
        season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f"Список сезонов - {season_1[int(user_month) // 3]}\nСловарь сезонов - {season_2[int(user_month) // 3]}")
        break
    else:
        print("Error")
