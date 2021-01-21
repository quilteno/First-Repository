filein = 'word.txt'
fileout = 'testout.txt'

string = [''] * 8                           #定义个列表,有8个字符串
count = 0                                   #计数器
with open(filein, 'r', encoding='UTF-8') as file:
    for line in file:                        #打开文件
        if count % 800 == 0 and count != 0:  #每20*5*8个单词为一个单位,即8个list
            with open(fileout, 'a') as out:    
                for i in range(0, 8):
                    out.write(string[i])
                    string[i] = ''           #写入拆分好的单词表后,清空缓存
        c = (int(count / 20)) % 8            #c为中间变量
        string[c] += line                    #每20列加到string0-7里
        count += 1
    with open(fileout, 'a') as out:  #末尾的单词也不要忘哦
        for i in range(0, 8):
            out.write(string[i])
