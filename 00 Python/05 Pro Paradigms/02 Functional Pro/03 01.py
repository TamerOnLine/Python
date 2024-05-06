temp = [("D", 29), ("A", 22), ("L", 18), ("E", 15), ("K", 35)]

print(type(temp))
# F = 1.8 * C + 32

def C_To_F(item):
    return item[0], (1.8) * item[1] + 32

f_temp = list(map(C_To_F, temp))

print(f_temp)









