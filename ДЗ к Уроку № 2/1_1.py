def div(arg_1, arg_2):
    try:
        arg_1, arg_2 = int(arg_1), int(arg_2)
        div_num = arg_1 / arg_2
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    return round(div_num, 2)


print(div(input('Введите первое число - '), input('Введите второе число - ')))