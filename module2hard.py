list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

numbers = int(input('Введите число от 3 до 20 из 1-го поля: '))

result = []

for j in range(1, len(list_)):
    for i in range(j + 1, numbers + 1):
        if numbers % (i + j) == 0:
            result += str(j) + str(i)

print(numbers, " - ", *result, sep='')
