my_list = [12, 10, 7, 5, 0, 4, 13, 8]
more_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_list)