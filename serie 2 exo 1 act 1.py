def flatten_ward(w_tuple) :
    tp = []
    for interval in w_tuple:
        car = interval[0]
        rep = interval[1]
        for i in range (rep) :
            tp.append(car)
    return "".join(tp)
w_tulpe = (("a",2),("b",4),("a",2),("b",6),("c",1))
print(flatten_ward(w_tulpe))