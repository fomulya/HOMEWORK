from functools import reduce

def first_list(el_1, el_2):
    return el_1 * el_2

second_list = [el for el in range(100, 1001, 2)]
print(f"List\n{second_list}\nNumber\n{reduce(first_list, second_list)}")



print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))