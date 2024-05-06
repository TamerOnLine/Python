numb = [1, 2, 2, 2, 4, 4, 5, 6, 7, 8, 8]
myset = set()
result = set()
for number in numb:
    if number in myset:
        result.add(number)
    myset.add(number)
print(result)