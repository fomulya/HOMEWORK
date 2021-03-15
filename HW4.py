from random import randint

first_list = [randint(0, 20) for _ in range(20)]
second_list = [el for el in first_list if first_list.count(el) == 1]
print(f'Начальный список\n{first_list}\nСписок без повторений\n{second_list}')


print(a := [randint(0, 9) for j in range(20)], '\n', [i for i in a if a.count(i) == 1], sep="")