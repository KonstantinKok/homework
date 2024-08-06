first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_ = zip(first, second)
first_result = ((len(x[0]) - len(x[1]) for x in first_ if len(x[0]) != len(x[1])))


second_result = ((len(first[y]) == len(second[y])) for y in range(len(first)))


print(list(first_result))
print(list(second_result))
