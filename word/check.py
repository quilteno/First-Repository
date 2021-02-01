import wordf

files = ['word']

for f in files:
    f = 'word/' + f + '.txt'
    with open(f, 'r', encoding='UTF-8') as file:
        for line in file:
            a = line[0:]
            if a < 'A' or a > 'z':
                print(a.rstrip(),end=' ')
        print('\r\r')
