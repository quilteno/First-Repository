import place

filename = 'word/word1.txt'  #输入文件
output = 'word/word2.txt'   #输出文件
WIDTH = 20             #一行中翻译开始的位置
key = ['n.','a.','v.','pron.','prep.','art.','ad.','aux.','vt.','num.','conj.','vi.','adj.','int.']

def main():
    with open(filename, 'r', encoding='UTF-8') as file: #读入文件,按行操作
        for line in file:
            len1 = len(line)
            with open(output,'a',encoding='UTF-8') as out:
                pl = 12
                for i in range(len(key)):     #查找字符串关键词
                    pls = serch(key[i],line)
                    if pls < pl:
                        pl = pls
                #print(pl,end='')             
                a = [line[0:pl]]
                b = [' ']
                c = [line[pl:len1+1]]
                a = a + b*(WIDTH-pl) + c#拼接字符串,在中间加上空格 
                if a[0][0] >='A' and a[0][0] <='z':#判断是否为单词，是则写入
                    for each in a:
                        out.write(each)

###查找关键词函数###
def serch(zi,mu):
    len1 = len(zi)
    pl = 20
    for i in range(len(mu)):
        if mu[i:i+len1] == zi:
            pl = i
            break
    return pl   
main()
