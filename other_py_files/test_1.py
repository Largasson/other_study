from collections import defaultdict


def task_1(d: dict):
    count_games = 0
    red, green, blue = 12, 13, 14
    for k, v in d.items():
        flag = True
        for game_iteration in v:
            dict_colors = defaultdict(int)
            for box in game_iteration.split(','):
                temp = box.strip().split(' ')
                dict_colors[temp[1].strip()] += int(temp[0].strip())
            if not (dict_colors['red'] <= red and dict_colors['green'] <= green and dict_colors['blue'] <= blue):
                flag = False
                break
        if flag:
            count_games += int(k.split(' ')[1])
    return count_games


def task_2(d: dict):
    sum_of_the_power = 0
    for k, v in d.items():
        dict_colors = defaultdict(int)
        for game_iteration in v:
            for box in game_iteration.split(','):
                temp = box.strip().split(' ')
                if dict_colors[temp[1].strip()] < int(temp[0].strip()):
                    dict_colors[temp[1].strip()] = int(temp[0].strip())
        power_color = dict_colors['red'] * dict_colors['green'] * dict_colors['blue']
        sum_of_the_power += power_color
    return sum_of_the_power


if __name__ == '__main__':
    with open('day2.txt', 'r', encoding='utf-8') as f:
        d = {line.split(':')[0]: line.split(':')[1].strip().split(';') for line in f.read().split('\n')}

    print(task_1(d))
    print(task_2(d))
