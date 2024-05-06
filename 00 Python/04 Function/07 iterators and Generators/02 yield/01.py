def mynumb(numb):
    for x in range(1, numb, 2):
        yield x

def myinfo(numb):
    for x in numb:
        yield x ** 2
        
#print(sum(myinfo(mynumb(24))))

print(sum(myinfo(mynumb(1050))))
        
