                       # 2. Работа со словарями:
# mi_dict = {"Вася" : 1975, "Егор" : 1999, "Маша" : 2002}
# print(f'Dict:{mi_dict}\n'
#      f'Existing value:{mi_dict["Маша"]}\n'
#      f'Not existing value:{mi_dict .get('Даша')}')
# mi_dict.update({"Камила": 1981,
#                "Артем" : 1915})
#a = mi_dict.pop("Егор")
#print(f'Deleted value:{a}\n'
#      f'Modified dictionary:{mi_dict}')

                       # 3. Работа с множествами:
mi_set = {13, 'Яблоко', 42.314, 13, 'Яблоко'}
print('Set:',mi_set)
mi_set.add((5, 6, 1.6))
print('Modified set:', mi_set)
mi_set.discard('Яблоко')                 # использую удаление без ошибки
print('Deleted value:', mi_set)





