def place(zi,mu):
    len1 = len(zi)
    pl = 20
    for i in range(len(mu)):
        if mu[i:i+len1] == zi:
            pl = i
            break
    return pl   