import wordf

f = 'word/final.txt'

with open(f, 'r', encoding='UTF-8') as file:
    for line in file:
        print(line[0].rstrip(),end='')
