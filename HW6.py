my_dict = {}
with open("hw6.txt", encoding="utf-8") as f:
    for line in f:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        my_dict[name] = name_sum
print(f"{my_dict}")