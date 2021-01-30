
filename = 'word1.txt'  #输入文件
output = 'word2.txt'  #输出文件


def main():
    with open(filename, 'r', encoding='ANSI') as file:  #读入文件,按行操作
        for line in file:
            if line[0] <'A' or line[0] >'z':
             
main()