import json

with open('companies.txt') as companies:
    i = 0
    profits = []
    firms = {}
    av_point = {}
    total = []
    for line in companies.readlines():
        line = line.split()
        profit = float(line[2]) - float(line[3])
        firms[line[0]] = profit
        if profit > 0:
            i += 1
            profits.append(profit)
    av_point['av_profit'] = round(sum(profits) / i, 2)
    total.append(firms)
    total.append(av_point)
print(total)

with open('companies_total.json', 'w') as companies_total:
    json.dump(total, companies_total)
