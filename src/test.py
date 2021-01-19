def main():
    string = 'hellor world!'
    pl = place('or',string)
    print(pl)

def place(zi,mu):
    len1 = len(zi)
    print(len1)
    pl = 8
    for i in range(len(mu)):
        if mu[i:i+len1] == zi:
            pl = i
            break
    return pl   

main()