goods = []
i = 0
while input('Хотите добавить новый товар? да/нет ') == 'да':
    i += 1
    number = i
    products = {'название': input('Введите название товара: '), 'цена': input('Введите цену товара: '),
                'количество': input('Введите количество товара: '), 'ед': input('Введите единицу измерения товара: ')}
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
