from itertools import combinations

def all_variants(text):
    lis = []
    for i in range(1, len(text)+1):
        lis = []
        b = combinations(text, i)
        lis.extend(b)
        for j in lis:
            j = list(j)
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    if i == 'ac':
        continue
    print(i)