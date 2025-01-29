from itertools import product

yo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

for i in product(yo[:int(input())], repeat=int(input())):
    print(''.join(i), end=' ')
