import os

name = os.listdir('word/EN')
filename = 'word/word4.txt'

for i in range(len(name)):
    name[i] = name[i].replace('.mp3','')
print(len(name))
