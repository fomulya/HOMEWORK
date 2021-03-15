from sys import argv

def salary():
    try:
        work, rate, bonus = map(float, argv[1:])
        print(f"Salary - {work * rate + bonus}")
    except ValueError:
        print("Введите данные для расчета")

salary()