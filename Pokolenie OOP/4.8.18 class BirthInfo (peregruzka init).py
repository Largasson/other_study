from functools import singledispatchmethod
from datetime import date, timedelta

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def from_strdate(self, birth_date):
        if len(birth_date) == 10 and birth_date.count('-') == 2:
            lst = birth_date.split('-')
            if len(lst[0]) == 4 and len(lst[1]) == len(lst[2]) == 2:
                self.birth_date = date.fromisoformat(birth_date)
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')


''' РЕШЕНИЕ от СОЗДАТЕЛЕЙ КУРСА'''
    # @__init__.register(str)
    # def str_init(self, birth_date):
    #     try:
    #         self.birth_date = date.fromisoformat(birth_date)
    #     except ValueError:
    #         raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(list)
    @__init__.register(tuple)
    def from_li_tu(self, birth_date):
        self.birth_date = date(birth_date[0], birth_date[1], birth_date[2])

    def get_age(self):
        return (date.today().toordinal() - self.birth_date.toordinal())//365.2

    age = property(get_age)

def current_age(birthday, today):   # функция проверки корректности даты от авторов курса
    age = today.year - birthday.year - 1
    age += (today.month, today.day) >= (birthday.month, birthday.day)
    return age




# # INPUT DATA:
#
# # TEST_1:
# birthinfo1 = BirthInfo('2020-09-18')
# birthinfo2 = BirthInfo(date(2010, 10, 10))
# birthinfo3 = BirthInfo([2016, 1, 1])
#
# print(birthinfo1.birth_date)
# print(birthinfo2.birth_date)
# print(birthinfo3.birth_date)
#
# # TEST_2:
# birthday = date(2020, 9, 18)
# today = date.today()
# birthinfo = BirthInfo(birthday)
# true_age = current_age(birthday, today)
#
# print(birthinfo.age == true_age)
#
# # TEST_3:
# birthinfo1 = BirthInfo('2020-09-18')
# birthinfo2 = BirthInfo(date(2010, 10, 10))
# birthinfo3 = BirthInfo([2016, 1, 1])
#
# print(type(birthinfo1.birth_date))
# print(type(birthinfo2.birth_date))
# print(type(birthinfo3.birth_date))
#
# # TEST_4:
# birthday = date(2023, 3, 6)
# today = date.today()
# birthinfo = BirthInfo(birthday)
# true_age = current_age(birthday, today)
#
# print(birthinfo.age == true_age)
#
# # TEST_5:
# errors = [20200918, True, {1: 'one'}, {1, 2, 3}, 100.9]
#
# for obj in errors:
#     try:
#         BirthInfo(obj)
#     except TypeError as e:
#         print(e)

# TEST_6:
today = date.today()
for day in range(10):
    birthday = (today + timedelta(days=day)).replace(year=2000)
    birthinfo = BirthInfo(birthday)
    true_age = current_age(birthday, today)
    print(birthinfo.age == true_age)

# TEST_7:
birth_dates = ['20200918', '2020-0918', '202009-18', ' 2020-09-18 ', '2020-9-18']

for birth_date in birth_dates:
    try:
        birthinfo1 = BirthInfo(birth_date)
    except TypeError as e:
        print(e)