def first():
    
    x = 100
    
    def last():
        
        nonlocal x
        
        x = 300
    
    last()
    
    print(x)

first()
       
