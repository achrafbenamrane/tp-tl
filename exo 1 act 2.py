
M1 = [2,4]
M2 = [3,5]
def repeatByList(a,b):
    M3 = []
    for i in range (len(M1)):
        e =[M1[i]]*M2[i]
        M3.append(e)
    print(M3)
repeatByList(M1,M2) 

