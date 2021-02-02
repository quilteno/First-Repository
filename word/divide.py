import wordf

filename = 'word/word.txt'
outfile1 = 'word/part1.txt'

wordf.delete([outfile1])

with open(filename,'r',encoding='UTF-8') as file:
    for line in file:
        if line[0] >= 'A':
            a = line[:20].replace(' ','')
            b = line[22:-4].replace(' ','')
            c = line[-4:].replace(' ','')
            a = a + '\t' + b + '\t' + c
            with open(outfile1,'a',encoding='UTF-8') as out1:
                out1.write(a)
