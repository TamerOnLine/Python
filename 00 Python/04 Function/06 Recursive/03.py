mybook = [('ru', 'zoo'), 'book one', 88, 40, ['thenn one', 'uuuz'], ' rtzu', 58]

def myinfo(list):
    if not list: return
    if (type(list[0]) == list or type(list[0]) == tuple):
        print(myinfo(list[0]))
    else:
        print(list[0])
        print(type(list))
    myinfo(list[1:])
    
myinfo(mybook)
