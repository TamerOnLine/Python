from datetime import date

while True:
    name = input('Enter your Name ')
    if name == 'stop':
        break
    age = input('Enter your Age ')
    print('Hallo', name)
    print('you are ' , 2024 - int(age))

