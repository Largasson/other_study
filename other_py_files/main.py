import csv

with open('student_counts.csv', 'r', encoding='utf-8') as file, \
        open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as outf:
    data = csv.DictReader(file)
    d = list(data)
    lst = data.fieldnames[1:]
    lst.sort()
    lst = sorted(lst, key= lambda x: int(x[:x.index('-')]))
    lst.insert(0, data.fieldnames[0])
    w = csv.DictWriter(outf, fieldnames=lst)
    w.writeheader()
    w.writerows(d)