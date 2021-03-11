def my_func(num1, num2, num3):
    list = [num1, num2, num3]
    return sum(sorted(list)[1:])

print(my_func(5, 9, 11))
