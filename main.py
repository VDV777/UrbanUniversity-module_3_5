# Напишите функцию get_multiplied_digits и параметр number в ней.
# Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
# 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять срез str_number[1:].
# Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.

def get_multiplied_digits(number: int) -> int:

    str_number: str = number.__str__()
    first: int = int(str_number[0])

    if str_number.__len__() > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print(get_multiplied_digits(12))
