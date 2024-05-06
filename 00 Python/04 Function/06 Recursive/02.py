mybook = ['ru', 'zoo', 'book one', 'thenn one']

def myinfo(list):
    if len(list) == 0:
        return
    else:
        print(list[0])
        return myinfo(list[1:])
myinfo(mybook)

