class Date:
    def __init__(self, my_date):
        self.my_date = str(my_date)

    @classmethod
    def extraction(cls, my_date):
        date, month, year = map(int, my_date.split('-'))
        return f'Date - {date}, month - {month}, year - {year}'

    @staticmethod
    def validate(date, month, year):
        if 0 < date <= 31:
            if 0 < month <= 12:
                if 0 < year <= 2020:
                    return 'Everything is right'
                return 'Wrong year'
            return 'Wrong month'
        return 'Wrong date'


today = Date('1-10-2020')
print(today.extraction('1-10-2020'))
print(today.validate(18, 13, 2016))
print(Date.extraction('6-4-2008'))
print(Date.validate(1, 12, 2020))
