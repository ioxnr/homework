with open('lessons.txt') as lessons:
    schedule = {}
    for line in lessons.readlines():
        line = line.split()
        total = 0
        for i in line:
            i = i.replace('(л)', '')
            i = i.replace('(пр)', '')
            i = i.replace('(лаб)', '')
            if i.isdigit():
                total += int(i)
        schedule[line[0]] = total
print(schedule)
