def info(name, surname, birthday, city, email, phone):
    return f"Имя - {name}; Фамилия - {surname}; Дата рождения - {birthday}; Город - {city};" \
    f"Email - {email}; Телефон - {phone};"

params = {
    'name': input('Введите Имя - '),
    'surname': input('Введите Фамилию - '),
    'birthday': input('Введите Дату рождения - '),
    'city': input('Введите город - '),
    'email': input('Введите email - '),
    'phone': input('Введите телефон - '),
    }
print(info(**params))