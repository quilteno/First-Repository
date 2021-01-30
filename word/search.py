import os

name = os.listdir('word/EN')
filename = 'word/word4.txt'
out = 'word/word4_lost.txt'

for i in range(len(name)):
    name[i] = name[i].replace('.mp3','')

with open(filename,'r',encoding='UTF-8') as file:
    for line in file:
        if line.rstrip()  not in name:
            with open(out,'a') as fileout:
                fileout.write(line)
            
