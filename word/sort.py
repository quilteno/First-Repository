import wordf

filename = 'word/core.txt'
outfile = '1.txt'
list1 = [] #定义空列表
def main():
    with open(filename,'r',encoding='UTF-8') as file:  #打开文件
        for line in file:  #遍历每行
            # print(takeElem(line))
            list1.append(line)
    list1.sort(key=takeElem)
    wordf.delete(['1.txt'])
    with open(outfile,'a',encoding='UTF-8') as out:  #打开文件
        list=''.join(list1)
        out.write(list.replace('/',''))

def takeElem(list):
    return list[-4:-1]

main()