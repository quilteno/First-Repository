import wordf

f = 'word/第一道工序.txt'

with open(f, 'r', encoding='UTF-8') as file:
    for line in file:
        if line[0] < 'A' or line[0] > 'z':
            print(line.rstrip(),end=' ')
