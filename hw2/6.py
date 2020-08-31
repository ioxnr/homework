goods = []
while input('Хотите добавить новый товар? да/нет ') == 'да':
    number = int(input('Введите номер товара: '))
    products = {}
    while input('Хотите ввести параметры товара? да/нет ') == 'да':
        product_key = input('Введите характеристику товара: ')
        product_value = input('Введите значение характеристики: ')
        products[product_key] = product_value
    goods.append(tuple([number, products]))
print(goods)
analitics = {}
for good in goods:
    for product_key, product_value in good[1].items():
        if product_key in analitics:
            analitics[product_key].append(product_value)
        else:
            analitics[product_key] = [product_value]
print(analitics)
