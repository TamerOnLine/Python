def get_Age():
    age = int(input('Enter: '))
    if age < 0:
        return
    if age > 120:
        return
    print(age)
get_Age()

