         # Кортеж. Тут написан код для изменения.

#immutable_var = 'Константин - молодец и учится на', 5, True
#print(immutable_var)
#immutable_var [2] = [False]

# Кортеж не изменяемый объект.
# Кортеж хранит ссылку на список, а не сам список.
# Если мы попытаетесь обратится к кортежу по индексу и заменить в нём какой-то элемент - это вызовет
# ошибку (например, ссылку на один список ссылкой на другой).


mutable_list = ['Константин - учится на', 2, True]
mutable_list[1] = 5
print(mutable_list)