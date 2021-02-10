import wordf

filename = 'word/word.txt'
keyname = 'word/a.txt'
outfile1 = 'word/filted.txt'

wordf.delete([outfile1])

def main():
    count = 0
    keys = keykey(keyname)
    for i in range(len(keys)):
        keys[i] = keys[i].replace(' ','').rstrip()
    print(keys)
    with open(filename,'r',encoding='UTF-8') as file:
        for line in file:
            line = line[:20].replace(' ','').rstrip()
            flag = 1
            for key  in keys:
                if key.replace(' ','') == line:
                    count += 1
                    flag = 0
            if flag == 1 and line >= 'A' and line <= 'z':
                with open(outfile1,'a',encoding='UTF-8') as out:
                    out.write(line)
                    out.write('\r')
        print(count)

def keykey(keysfile):
    with open(keysfile,'r',encoding='UTF-8') as keys:
        keyList = []
        for key in keys:
            keyList.append(key)
    return keyList    

main()