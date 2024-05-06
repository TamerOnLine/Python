def myM(numb):
    for x in numb:
        yield x

def myH(numb):
    for x in numb:
        yield x ** 2
        
print(sum(myinfo(mynumb(24))))

