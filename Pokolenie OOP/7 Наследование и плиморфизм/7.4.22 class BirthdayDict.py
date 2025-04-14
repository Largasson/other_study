from collections import UserDict
from datetime import date


class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        processed_birthdays = set()
        for existing_key, existing_value in self.items():
            if (existing_value.day, existing_value.month) == (value.day, value.month) and (
            existing_value.day, existing_value.month) not in processed_birthdays:
                print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
                processed_birthdays.add((existing_value.day, existing_value.month))
        super().__setitem__(key, value)




names = ['Измаил', 'Рюрик', 'Фортунат', 'Сила', 'Ирина', 'Оксана', 'Ипатий', 'Регина', 'Никифор', 'Валерия', 'Эмилия',
         'Порфирий', 'Христофор', 'Герман', 'Иванна', 'Елизар', 'Рубен', 'Сидор', 'Демьян', 'Прохор', 'Элеонора',
         'Милий', 'Марфа', 'Любомир', 'Пелагея', 'Дарья', 'Иосиф', 'Феврония', 'Андроник', 'Ростислав', 'Фаина', 'Боян',
         'Ульяна', 'Николай', 'Григорий', 'Лора', 'Антонина', 'Аггей', 'Бронислав', 'Олимпиада', 'Александра',
         'Евпраксия', 'Ким', 'Еремей', 'Пимен', 'Казимир', 'Фотий', 'Любим', 'Майя', 'Поликарп', 'Клавдия', 'Филипп',
         'Павел', 'Ангелина', 'Станислав', 'Раиса', 'Ольга', 'Назар', 'Добромысл', 'Агата', 'Ладислав', 'Ия', 'Наина',
         'Юлиан', 'Анастасия', 'Акулина', 'Иван', 'Евсей', 'Евдоким', 'Галина', 'Владислав', 'Синклитикия', 'Ираида',
         'Ратибор', 'Юлий', 'Стоян', 'Глафира', 'Панкратий', 'Кира', 'Мстислав', 'Алевтина', 'Виктория', 'Людмила',
         'Октябрина', 'Прасковья', 'Радислав', 'Влас', 'Анжела', 'Ксения']

birth_dates = [date(2018, 2, 3), date(2006, 1, 25), date(1981, 12, 27), date(2005, 5, 26), date(1977, 9, 3),
               date(2021, 4, 26), date(2014, 11, 10), date(2004, 2, 5), date(2000, 10, 9), date(2022, 7, 14),
               date(1974, 6, 2), date(1978, 1, 6), date(2018, 9, 23), date(2001, 8, 1), date(1999, 3, 11),
               date(1984, 7, 7), date(1995, 2, 15), date(1986, 3, 17), date(2009, 2, 16), date(2010, 4, 11)]

birthdaydict = BirthdayDict()

for name, birth_date in zip(names, cycle(birth_dates)):
    birthdaydict[name] = birth_date
