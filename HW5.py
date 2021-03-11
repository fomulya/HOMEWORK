def sum_num():
    a = 0
    while True:
        list = input('Введите число или X для выхода: ').split()
        for num in list:
            if num == 'X':
                return a
            else:
                try:
                    a+= int(num)
                except ValueError:
                    print('Для выхода из программы нажмите X - ')

        print(f'Сумма чисел = {a}')
num = 0
try:
    while num != 'X':
        for i in map(int, input("Введите число или X для выхода - ").split()):
            num += i
        print(num)
except ValueError:
    print(num)