def file2list(filename):
    filelist = []
    file = open(filename, "r")
    for line in file.readlines():
        for word in line.split():
            filelist.append(word)
    return filelist

print(file2list('texto.txt'))
