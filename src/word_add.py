filename = '121.txt'  #输入文件
output = 'word3.txt'  #输出文件


def main():
    with open(filename, 'r', encoding='ANSI') as file:  #读入文件,按行操作
        count = 0
        for line in file:
            count = count + 1
            if line[0] <'A' or line[0] >'z':
                print(count)
main()