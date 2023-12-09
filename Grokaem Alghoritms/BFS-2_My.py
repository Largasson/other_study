from collections import deque


def person_is_req(name):
    return True if name == 'Ольга' else False

def serch_BFS(graph, start, end):
    ochered = deque()  # инициализация очереди
    ochered += d[start]  # подаем в очередь начальную вершину
    checked_person = {}  # словарь с проверенными вершинами-людьми, в будущем поможет построить дорогу обратно
    checked_person[start] = None
    while ochered:
        person = ochered.popleft()
        if person == end: # определили, что нашли нужного человека
            path = []   # создаем переменную для хранения пути
            while person not in d[start]:   # строим путь обратно
                path.append(person)   # добавляем вершину
                person = checked_person[person]   # получаем родителя этой вершины - переходим на уровень выше
            path.append(person)
            path.append(start)
            return list(reversed(path))  # возвращаем путь
        for friends in graph.get(person, []):   # перебираем друзей   d.get(person, [])
            if friends not in checked_person:
            #    checked_person[person] =
                ochered.append(friends)   #   добавляем в очередь тех кого еще не проверили
                checked_person[friends] = person   #   добавляем в словарь проверенных
    return None


d = {'Я': ['Ярик', 'Лида', 'Сережа', 'Марина', 'Вова'],
     'Ярик': ['чел 3', 'Трофим'],
     'Лида': ['Семен'],
     'Сережа': ['Трофим', 'Семен'],
     'Марина': ['Лена'],
     'Вова': ['чел 1', 'чел 2'],
     'Семен': ['Лена'],
     'Лена': ['Ольга']}

# start_node = list(graph.keys())[0]

start_node = 'Я'
end_pose = 'Ольга'  # ищем Ольгу


path = serch_BFS(d, start_node, end_pose)
if path:
    print(*path, sep='-->')
else:
    print('нет такой')
