file = open('hello.txt', 'r')

for line in file.readlines():
    print(line.strip())

file.close()
