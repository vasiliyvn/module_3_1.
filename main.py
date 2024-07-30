def count_calls(call):  # кщличество вызовов
    global calls
    calls += call
    return calls


def string_info(string):  #инфорация о строке
    a=[]
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    count_calls(1)
    return a


def is_contains(string_info, is_contains): #содержит
    string_info.lower()
    list_to_search = []
    count_calls(1)
    for i in is_contains:
        list_to_search.append(i.lower())
    return (string_info.lower() in list_to_search)


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
