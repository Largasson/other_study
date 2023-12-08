with open('elf_in.txt', 'r') as file:
    data = file.read()
    data = data.split('\n\n')
    lst = []
    for line in data:
        temp = sum(list(map(int, line.split())))
        lst.append(temp)
    print(sum(sorted(lst,reverse=True)[:3]))

