def calculate_structure_sum(*args):
    number = 0
    for i in args:
        if isinstance(i, int):
            number += i
        elif isinstance(i, str):
            number += len(i)
        elif isinstance(i, (list, tuple, set)):
            number += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            number += calculate_structure_sum(*i.items())
    return number


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
