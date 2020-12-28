def main():
    pi(1000000000)


def pi(num):
    flag = 1
    sum = 0
    for n in range(1, num):
        sum +=1/(flag*(2*n-1))
        flag=-flag
    print(f"pi={sum*4}")
    
main()