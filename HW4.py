russian_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
with open("hw4_new.txt", "w", encoding="utf-8") as file_new:
    with open("hw4.txt", "r", encoding="utf-8") as file_my:
        file_new.write(str([line.replace(line.split()[0], russian_dict.get(line.split()[0])) for line in file_my]))

