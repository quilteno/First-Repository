def main():
    try:
        print(5/1)
    except ZeroDivisionError:
        print("You can't divide by Zero!")
    #birthday = input("Enter your birthday:")
    #piSearch(birthday)
def piSearch(number):
    filename = 'Pi.txt'
    with open(filename) as file_Pi:
        i = 0
        for line in file_Pi:
            i += 1
            if number in line:
                print(f"Your birthday is in {len(line)}")
            else:
                print("No")    
    
main()