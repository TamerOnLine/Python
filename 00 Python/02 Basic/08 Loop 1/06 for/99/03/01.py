numb = [1, 2, 2, 2, 4, 4, 5, 6, 7, 8, 8]


mylist = []
myset = set()

for x in numb:
    if x in myset:
        mylist.append(x)
    myset.add(x)
print(mylist)
    





