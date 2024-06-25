class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
            return
        for new_floor in range(1, new_floor + 1):
            print(new_floor)


h1 = House('ЖК Горский', 18)
# print(h1.name, h1.number_of_floors)
h1.go_to(5)
h2 = House('Домик в деревне', 2)
# print(h2.name, h2.number_of_floors)
h2.go_to(10)
