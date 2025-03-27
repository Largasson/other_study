def  non_closed_files(files:list):
    rez_lst = []
    for file in files:
        if not file.closed:
            rez_lst.append(file)
    return rez_lst