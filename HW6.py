def int_func(text):
    latin_leters = "qwertyuiopasdfghjklzxcvbnm"
    return text.title() if not set(text).difference(latin_leters) else False

words = input('Введите строку из слов, разделенных пробелами - ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')