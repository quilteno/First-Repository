filein = 'word1111.txt'
fileout = 'testout.txt'

with open(filein, 'r',encoding='UTF-8') as file:
    count = 0
    pl = 0
    for line in file:
        try:
            pls = line.index(' ')
            if pls > pl:
                pl = pls
                a = count
        except ValueError:
            pass    
        count += 1
    print(a)
    print(pl)
