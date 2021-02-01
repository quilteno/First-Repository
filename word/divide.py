import wordf

filename = 'word/1.txt'
outfile1 = 'word/part1.txt'
outfile2 = 'word/part2.txt'

wordf.delete(outfile1)
wordf.delete(outfile2)
AA = 26
with open(filename,'r',encoding='UTF-8') as file:
    for line in file:
        a = line[:AA]
        b = line[AA:]
        with open(outfile1,'a',encoding='UTF-8') as out1:
            out1.write(a.replace(' ',''))
            out1.write('\r')
            out1.close()
        with open(outfile2,'a',encoding='UTF-8') as out2:
            out2.write(b.replace(' ',''))
            out2.close()
