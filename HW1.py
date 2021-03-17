with open("hw1.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("Введите новую строку - ")
        if not line:
            break
        print(line, file=f)
