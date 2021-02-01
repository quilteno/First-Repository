import wordf

filename = 'word/word.txt'
outfile1 = 'word/part1.txt'
outfile2 = 'word/part2.txt'
outfile3 = 'word/part3.txt'

wordf.delete([outfile1,outfile2,outfile3])

with open(filename,'r',encoding='UTF-8') as file:
    for line in file:
        if line[0] >= 'A':
            a = line[:26]
            b = line[26:-4]
            c = line[-4:]
            with open(outfile1,'a',encoding='UTF-8') as out1,\
                open(outfile2,'a',encoding='UTF-8') as out2,\
                    open(outfile3,'a',encoding='UTF-8') as out3:
                out1.write(a.replace(' ',''))
                out1.write('\r')
                out2.write(b.replace(' ',''))
                out2.write('\r')
                out3.write(c.replace(' ',''))
