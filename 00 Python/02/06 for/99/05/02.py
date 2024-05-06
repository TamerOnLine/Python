numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
mynumb = []
mynumb2 = []
for i in range(0,len(numb),4):
    mynumb2.append(i)
    print(i)
    
    mynumb.append(numb[i:i+3])
print(mynumb)
print(mynumb2)


    
    
    
    
