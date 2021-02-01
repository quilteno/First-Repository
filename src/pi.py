
def main():
    a = 1
    for i in range(1000):
        for j in range(1000):
            for k in range(200):
                    a += a
                    a = a/2
                    
    #birthday = input("Enter your birthday:")
    #piSearch(birthday)
#def piSearch(number):
#    filename = 'Pi.txt'
#    with open(filename) as file_Pi:
#        i = 0
#        for line in file_Pi:
#            i += 1
#            if number in line:
#                print(f"Your birthday is in {len(line)}")
#            else:
#                print("No")    
    
main()