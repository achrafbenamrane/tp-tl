def crange(*cintrev):
    result_list= []
    for liste in cintrev:
        for i in range(ord(liste[0]),ord(liste[1])+1):
            result_list.append(chr(i))
    return "".join(result_list)
print("alphabet:",crange(["0","9"]))  
print("numero :",crange(["A","Z"]))
       