filename = 'word/word2.txt'
outfile = 'word/word2_fixed.txt'

#delete(outfile)

with open(filename,'r',encoding='UTF-8') as file:
    for line in file:
        line = line[:20] + line[20:].replace(' ','')
        line = line.replace('，',',')
        line = line.replace('；',';')
        line = line.replace('．','.')
        with open(outfile,'a',encoding='UTF-8') as out:
            out.write(line)
