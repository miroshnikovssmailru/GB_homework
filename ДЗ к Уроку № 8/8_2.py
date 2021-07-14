class DivisionByZeroException(Exception):
    def __init__(self, *args: object) -> None:
         super().__init__('На 0 делить нельзя!')

def div(value1: int, value2: int) -> float:
    if value2 == 0:
        raise DivisionByZeroException()
    return value1 / value2

while (i := input('Введите делитель для 100: ')) != '':
    try:
        print(f'Результат: {div(100, int(i))}')
    except DivisionByZeroException as e:
        print(e)
    except ValueError:
        pass