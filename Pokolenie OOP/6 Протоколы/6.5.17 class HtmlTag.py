class HtmlTag:
    global_level = -1  # Общий уровень вложенности

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        HtmlTag.global_level += 1  # Увеличиваем уровень вложенности
        if not self.inline:
            print('  ' * HtmlTag.global_level + f"<{self.tag}>")  # Открывающий тег на отдельной строке
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.inline:
            print('  ' * HtmlTag.global_level + f"</{self.tag}>")  # Закрывающий тег на отдельной строке
        HtmlTag.global_level -= 1  # Уменьшаем уровень вложенности

    def print(self, text):
        if self.inline:
            # Печатаем открывающий тег, текст и закрывающий тег на одной строке
            print('  ' * HtmlTag.global_level + f"<{self.tag}>{text}</{self.tag}>")
        else:
            # Печатаем текст внутри открытого тега с дополнительным отступом
            print('  ' * (HtmlTag.global_level + 1) + text)

# INPUT DATA:

# TEST_1:
with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

# TEST_2:
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')

# TEST_3:
with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Здесь есть что-то интересное')
    with HtmlTag('a', True) as section:
        section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')

# TEST_4:
with HtmlTag('div') as _:
    with HtmlTag('p') as paragraph:
        with HtmlTag('strong', True) as strong:
            strong.print('Notice:')
        paragraph.print('Your browser is ancient')

# TEST_5:
with HtmlTag('table') as _:
    with HtmlTag('tr') as paragraph:
        with HtmlTag('th', True) as field:
            field.print('текст заголовка')
        with HtmlTag('td') as data:
            with HtmlTag('ul'):
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')