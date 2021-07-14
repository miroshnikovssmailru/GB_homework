class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        list = []

        if 1 > day or day > 31:
            list.append(f'Ошибка! значение "день" введено неверно.')
        if 1 > month or month > 12:
            list.append(f'Ошибка! значение "месяц" введено неверно.')
        if 0 >= year:
            list.append(f'Ошибка! значение "год" введено неверно.')
        if len(list) > 0:
            return " ".join(list)
        else:
            return f'Введены верные значения даты.'


def __str__(self):
    return f'Текущая дата - {Data.extract(self.day_month_year)}'

today = Data('09 - 05 - 1945')
print(today)

print(Data.valid(1, 4, 2000))
print(today.valid(33, 18, -123))

