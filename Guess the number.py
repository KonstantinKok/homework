import random

numbers = random.randint(1, 500)
c = 0
for j in range(numbers):
    i = int(input('Введите число от 1 до 500 '))
    if i == numbers:
        print(f'Вы угадали число за {c} ходов!!!')
    elif i > numbers:
        print('Ваше число больше загаданного')
    elif i < numbers:
        print('Ваше число меньше загаданного')
    c += 1
    continue
