from itertools import count, cycle

print("Для генерации стартового числа нажмите Enter, для выхода нажмите х")
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'x':
        break

print("Для генерации следующего повторения нажмите Enter, для выхода нажмите х")
my_list = input('Введите список, разделяя элементы пробелом: ').split()
iter_ = cycle(my_list)
quit = None

while quit != 'х':
    print(next(iter_), end='')
    quit = input()