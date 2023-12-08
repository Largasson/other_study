from collections import deque


def person_is_req(name):
    return True if name == 'Ольга' else False


d = {'Я': ['Ярик', 'Лида', 'Сережа', 'Марина', 'Вова'],
     'Ярик': ['чел 3', 'Трофим'],
     'Лида': ['Семен'],
     'Сережа': ['Трофим', 'Семен'],
     'Марина': ['Ольга', 'Лена'],
     'Вова': ['чел 1', 'чел 2']}



def serch_BFS(name):
    ochered = deque()
    ochered += d[name]
    last_person = []
    lst_range = []
    k = 0
    while ochered:
        person = ochered.popleft()
        k += 1
        if person not in last_person:
            if person_is_req(person):
                return f'Нашлась пропажа, количество проверенных веток - {k}, person = {person}'
            else:
                ochered += d.get(person, [])
                last_person.append(person) # должен быть словарь. last_person[person] =
    return f'Обошли все дерево, не нашли'

print(serch_BFS('Я'))
