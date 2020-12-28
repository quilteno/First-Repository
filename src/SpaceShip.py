from time import sleep
def main():
    i=1
    j=1
    filename = 'numebr.txt'
    while True:
        i*=2
        j+=1
        with open(filename,'a') as file_object:
            file_object.write(f"2^{j}={i}\n")
        sleep(0.001)
main()
