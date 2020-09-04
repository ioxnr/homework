def data(name, surname, date_of_birth, city, email, phone_number):
    return ' '.join([name, surname, date_of_birth, city, email, phone_number])


print(data(name=input('Введите свое имя: '),
           surname=input('Введите свою фамилию: '),
           date_of_birth=input('Введите год рождения: '),
           city=input('Введите город проживания: '),
           email=input('Введите свой email: '),
           phone_number=input('Введите номер телефона: ')))
