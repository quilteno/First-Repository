import wordf

filename = 'word/base.txt'
outfile = 'word/2.txt'

wordf.delete([outfile])
list = ''
with open(filename, 'r', encoding='UTF-8') as file:
    for line in file:
        # line = line.replace('口', '')
        # line = line.replace('prep.', '')
        # line = line.replace('n.', '')
        # line = line.replace('ad.', '')
        # list = list.join(line)
        if line[1] >= 'A' and line[1] <= 'z' and line[0] == ' ':
            with open(outfile, 'a', encoding='UTF-8') as out:
                out.write(line.replace(' ',''))
