from pprint import pprint

# Для проверки создать чистый файл products.txt, либо скачать по ссылке

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):    #возвращает строку в формате '<название>, <вес>, <категория>'
        return f'{self.name}, {self.weight}, {self.category}.'


class Shop:
    
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):
        data = self.get_products()
        new_data = ''
        for i in products:
            if i.name in data + new_data:
                print(f'Продукт {i.name} уже есть в магазине.')
            else:
                new_data += str(i) + '\n'
        if new_data:
            file = open(self.__file_name, 'a')
            file.write(new_data)
            file.close()






p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

Shop().add(p1, p2, p3)

print(Shop().get_products())
