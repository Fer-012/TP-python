def DistanceHamming(ch1,ch2):
    occ = 0
    if len(ch1) != len(ch2):
        return -1
    else:
        for i in range (len(ch1)):
            if ch1[i] != ch2[i]:
                occ += 1
    return occ


ch1 = input("entrez la 1er chaine : ")
ch2 = input("entrez la 2eme chaine : ")
print(DistanceHamming(ch1, ch2))
