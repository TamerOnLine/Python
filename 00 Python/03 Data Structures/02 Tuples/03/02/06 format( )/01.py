myf = 'Hallo {}'
x = input(' Enter your Name: ')

myfname = myf.format(x)
print(type(myfname), end = ' format()') == print(myfname)
