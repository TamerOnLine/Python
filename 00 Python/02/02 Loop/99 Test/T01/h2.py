x = int(input('Enter number = '))
if x < 0 or x > 100:
    print('Err')
    exit()
if 89 < x < 101:
    print('A')
elif 79 < x < 90:
    print('B')
elif 69 < x < 80:
    print('C')
elif 59 < x < 70:
    print('D')
elif 49 < x < 60:
    print('E')
elif 0 <= x < 50:
    print('F')