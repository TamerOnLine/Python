numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

mynumb = [numb[i:i+3] for i in range(0,len(numb), 3)]

print(mynumb)

