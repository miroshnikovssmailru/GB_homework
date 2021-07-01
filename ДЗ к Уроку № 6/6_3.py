class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name}{self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"

engeneer = Position('Ivan', ' Ivanov', 'Engeneer', 25000, 50000)
print(engeneer.get_full_name())
print(engeneer.position)
print(engeneer.get_full_profit())