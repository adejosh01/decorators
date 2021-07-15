def bank(dec1, dec2):
    def Bank(func):
        def wrapper(func1, func2):
            print('This is my first choice of {} :{} at {} and my second choice is {} at {}  '.format(func.__name__, dec1, dec2, func1, func2))
            return func(func1, func2)
        return wrapper
    return Bank

#This will collect my first choice of bank and the location

dec1 = input('Enter your first choice of bank here: ')
dec2 = input('Enter the location here: ')
@bank(dec1 , dec2)
def bank_list2(func1, func2):
    print('My bank is {} at {}'.format(func1, func2))

#This will collect my second choice of bank

func1 = input('Enter your second choice of bank here: ')
func2 = input('Enter your location here: ')

bank_list2(func1, func2)