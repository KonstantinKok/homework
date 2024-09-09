import calk

def test_add():
    if calk.add(1,2) == 3:
        print('Функция + работает ВЕРНО')
    else:
        print('Функция + работает НЕ ВЕРНО')

def test_sub():
    if calk.sub(2,1) == 1:
        print('Функция - работает ВЕРНО')
    else:
        print('Функция - работает НЕ ВЕРНО')

def test_mul():
    if calk.mul(2,2) == 4:
        print('Функция * работает ВЕРНО')
    else:
        print('Функция * работает НЕ ВЕРНО')

def test_div():
    if calk.div(2,1) == 2:
        print('Функция / работает ВЕРНО')
    else:
        print('Функция / работает НЕ ВЕРНО')

test_add()
test_sub()
test_mul()
test_div()
