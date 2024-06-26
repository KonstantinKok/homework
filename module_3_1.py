calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    return length, string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    new_string = string.lower()
    new_list = [x.lower() for x in list_to_search]
    if new_string in new_list:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
