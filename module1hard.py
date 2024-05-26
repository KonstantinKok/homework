diary_dict = {}    # Переменная словаря

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))    # Упорядоченный по алфавиту список студентов из множества
grades_average_list = [(sum(grades[0]) / len(grades[0])),
                       (sum(grades[1]) / len(grades[1])),
                       (sum(grades[2]) / len(grades[2])),
                       (sum(grades[3]) / len(grades[3])),
                       (sum(grades[4]) / len(grades[4]))]

# Создание словаря
diary_dict[students_list[0]] = grades_average_list[0]
diary_dict[students_list[1]] = grades_average_list[1]
diary_dict[students_list[2]] = grades_average_list[2]
diary_dict[students_list[3]] = grades_average_list[3]
diary_dict[students_list[4]] = grades_average_list[4]
print(diary_dict)
