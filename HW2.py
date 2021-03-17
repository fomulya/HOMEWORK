my_lines = 0
my_words = 0
f = open("hw2.txt", "r")
for line in f:
    my_lines += 1
    words = line.split()
    my_words += len(words)
print(my_lines)
print(my_words)
