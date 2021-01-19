filein = 'test.txt'
fileout = 'testout.txt'

with open(filein, 'r',encoding='UTF-8') as file:
    count = 0
    
    string1 = string2 = ''
    for line in file:
        #print(f"{'*'}{int((count / 10)) % 2}")
        if int((count / 10)) % 2 == 0:
            string1 += line
        elif int((count / 10)) % 2 == 1:
            string2 = line + string2
            #print(string2)
        if (count) % 320 == 0 and count != 0:
            with open(fileout,'a') as out:
                print(string1[:20] + string2[:20])
                out.write(string1 + string2)
            string1 = string2 = ''
        count += 1
    with open(fileout,'a') as out:
            out.write(string1 + string2)