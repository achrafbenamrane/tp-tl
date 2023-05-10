def simulate_fsa(word):
    alphabet=["a","b","c","d"]
    state = 3

    for i in range (len(word)):
        if (word[i] not in alphabet):
            return False
        else:
            if ( state == 0 ):
                if (word[i]=="a"):
                    state+=1  
            if (state == 1):
                if (word[i]=="b"):
                    state+=1
                elif (state == 1):
                    if(word[i]=="c" or word[i]=="d"):
                        state-=1
            if (state == 2 ):
                if (word[i]== "c"):
                    state+=1
            if (state == 3 ):
                if (word[i]== "d"):
                    state+=1
                elif (word[i]== "a" ):
                    state-=1
    if (state==4):
        return True
    else:
        return False

print(simulate_fsa("cdbaabbcdb"))