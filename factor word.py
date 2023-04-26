def factors (word):
    L = [""]
    for i in range (len (word)):
        for j in range (i,len(word)):
            if word [i : j+1] not in L:
              L.append(word[i:j+1])
    return L
      
print(factors("aaaabbbbcccc"))