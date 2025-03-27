def log_for(logfile, date_str):
    filename = 'log_for_' + date_str + '.txt'
    with (
        open(filename, 'w', encoding="utf-8") as outfile,
        open(logfile, 'r', encoding="utf-8") as logfile
    ):
        for line in logfile:
            if date_str in line:
                outfile.write(line[11:])



with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())