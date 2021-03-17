with open("hw3.txt", "r", encoding="utf-8") as f:
    salary = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя заработная плата = {round(sum(salary.values()) / len(salary), 5)}\n'
        f'Сотрудники с заработной платой менее 20 тысяч {[e[0] for e in salary.items() if e[1] < 20000]}')