x = int(input('Enter number = '))
if x < 0 or x > 100:
    print('Err')
    exit()
if x in range(90, 101):
    print('A')
elif x in range(80, 90):
    print('B')
elif x in range(70, 80):
    print('C')
elif x in range(60, 80):
    print('D')
elif x in range(50, 60):
    print('E')
elif x in range(0, 50):
    print('F')
