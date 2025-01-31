class Worker:
    def __init__(self, name, surname, age, salary, position='worker'):
        self._salary = salary
        self._name = name
        self._surname = surname
        self._age = age
        self._position = position

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    name = property(get_name, set_name, doc='Свойство, отвечающее за атрибут имени')

    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        if isinstance(surname, str) and surname.isalpha():
            self._surname = surname
        else:
            ValueError('Некорректная фамилия')

    surname = property(get_surname, set_surname, doc='Свойство, отвечающее за атрибут фамилии')

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and age >= 16:
            self._age = age
        elif isinstance(age, int) and 0 < age < 16:
            raise ValueError('Малолеток не берем')
        else:
            raise ValueError('Некорректно введен возраст')

    age = property(get_age, set_age, doc='Свойство, отвечающее за атрибут возраста')

    def get_position(self):
        return self._position

    def set_position(self, position):
        if isinstance(position, str) and position.isalpha():
            self._position = position
        else:
            raise ValueError('Некорректно введены данные')

    position = property(get_position, set_position, doc='Свойство, отвечающее за атрибут должности')

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if isinstance(salary, int) and salary > 0:
            self._salary = salary
        else:
            raise ValueError('Вы ввели некорректные данные по зарплате')

    salary = property(get_salary, set_salary, doc='Свойство, отвечающее за атрибут Зарплаты')

    def get_info(self):
        return f'{self.name} {self.surname} {self.age} {self.position} {self.salary}'

    info=property(get_info, doc='Свойство, отвечающее за общую информацию о работнике')

Alex = Worker('Alex', 'Sedov', 19, 100000)
print(Alex.name)
print(Alex.surname)
print(Alex.age)
print(Alex.position)
print(Alex.salary)
print(Alex.info)
print(Alex.__dict__)