f1 = open('f1.txt','r')
f2 = open('fu.txt','w')

for line in f1.readlines():
    if not(line.startswith('hello')):
        print(line)

        f2.write(line)
f2.close()
f1.close()

