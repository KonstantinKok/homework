first, second, third = (int(input('Введите первое число: ')),
                        int(input('Введите второе число: ')),
                        int(input('Введите третье число: ' )))
if first == second == first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
elif first != second != third:
    print('0')
