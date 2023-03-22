L1 = [1,2,5,9]
L2 = [2,9]
def substruct(L1,L2):
    for i in range (len(L2)):
        if L2[i] in L1: 
            L1.remove(L2[i])
    print(L1)
substruct(L1,L2)