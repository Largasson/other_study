from collections import deque
def BFS(graph, start, stop):
    deq = deque()
    deq.extend(graph[start])
    verified = dict.fromkeys(deq, start)
    verified[start] = None
    while deq:
        chel = deq.popleft()
        if chel == stop:
            path = []
            while chel is not None:
                path.append(chel)
                chel = verified[chel]
            return list(reversed(path))
        for friend in graph.get(chel, []):
            if friend not in verified:
                deq.append(friend)
                verified[friend] = chel
    return

if __name__ == "__main__":
    d = {'Я': ['Ярик', 'Лида', 'Сережа', 'Марина', 'Вова'],
         'Ярик': ['чел 3', 'Трофим'],
         'Лида': ['Семен'],
         'Сережа': ['Трофим', 'Семен'],
         'Марина': ['Лена', 'Ольга'],
         'Вова': ['чел 1', 'чел 2'],
         'Семен': ['Лена'],
         'Лена': ['Ольга']}

    start_pos = 'Я'
    end_pos = 'Ольга'

    p = BFS(d, start_pos, end_pos)

    if p:
        print(f'путь - {p}')
    else:
        print('нет пути')
