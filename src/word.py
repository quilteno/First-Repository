import place

filename = 'word.txt'  #输入文件
output = 'word4.txt'   #输出文件
WIDTH = 20             #一行中翻译开始的位置
key = ['n.','a.','v.','pron.','prep.','art.','ad.','aux.','vt.','num.','conj.','vi.','adj.']

def main():
    with open(filename, 'r', encoding='UTF-8') as file: #读入文件,按行操作
        for line in file:
            len1 = len(line)
            with open(output,'a') as out:
                pl = 12
                for i in range(len(key)):
                    pls = place(key[i],line)
                    if pls < pl:
                        pl = pls
                #print(pl,end='')             
                a = [line[0:pl]]
                b = [' ']
                c = [line[pl:len1+1]]
                a = a + b*(WIDTH-pl) + c      #拼接字符串,在中间加上空格 
                for each in a:
                    out.write(each)

main()
