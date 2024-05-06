



def square_num(num):
    
  
         return num ** 2
       


def main():
    numbers = range(1, 10 , 2)
    squared_numbers = map(square_num, numbers)

    
    for num in squared_numbers:
        

        print(num)

main()

          


