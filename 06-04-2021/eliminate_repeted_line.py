f2 = open('file2.txt', 'w')
f1 = open('file1.txt', 'r')
allready_writen_line = set()

for line in f1:
    if line not in allready_writen_line:
        f2.write(line)
        allready_writen_line.add(line)
f1.close()
f2.close()
