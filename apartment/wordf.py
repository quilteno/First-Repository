import os

def delete(paths):
    '''
    文件目录,用于删除文件
    '''
    for path in paths:
        if os.path.exists(path):  # 如果文件存在
            # 删除文件
            os.remove(path)
            print('我删掉重新来了哦')
        else:
            print('文件不在啊')  # 则返回文件不存在 
     
def serch(son, mother):
    '''
    关键字,原文
    '''
    len1 = len(son)
    pl = 20
    for i in range(len(mother)):
        if mother[i:i + len1] == son:
            pl = i
            break
    return pl

def style(key,line,width):
    '''
    词性列表,原列,扩充为多少
    '''            
    pl = 15
    len1 = len(line)
    for i in range(len(key)):  #查找字符串关键词
        pls = serch(key[i], line)
        if pls < pl:
            pl = pls
    a = [line[0:pl]]
    b = [''.join(' ')*(width-pl)]
    c = [line[pl:len1 + 1]]
    a = a + b + c  #拼接字符串,在中间加上空格
    return a