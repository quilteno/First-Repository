number = 41153243
flag = 1
for i in range(2,number):
    if number % i == 0:
        flag = 0
        print(f'{number}={i}*{number/i}')
        break
if flag:
    print('没有质数')