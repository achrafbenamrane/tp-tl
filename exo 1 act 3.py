liste=[1,3,5,7,9,8,6,4,2]
def symmetric_achraf(L):
        resL = []
        for i in range(int(len(L)/2+1)):
                resL.append(L[i])
                if i != int(len(L)/2):
                        resL.append(L[len(L)-1-i])
        return resL                                   
print("resultat est :" , symmetric_achraf(liste))               
