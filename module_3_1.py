calls = 0


# подсчитывающая вызовы остальных функций


def count_calls():
    global calls


# принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.


def string_info(string):
    string.upper()
    string.lower()


# принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.


def is_contains(string, list_to_search):
    pass


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)

# Вывод на консоль:
# (8, 'CAPYBARA', 'capybara')
# (10, 'ARMAGEDDON', 'armageddon')
# True
# False
# 4
# Примечания:
# Для использования глобальной переменной внутри функции используйте оператор global.
# Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.
