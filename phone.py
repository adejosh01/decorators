def phone(func):
    def wrapper(func1, func2):
        print('checking the details of {} and the num: {}'.format(func1, func2))
        return func(func1, func2)
    return wrapper

@phone
def phone_check(name, num:str):
    if len(num) == 11 or num.startswith('+234'):
        print("Going through...")
    else:
        print("hang up...")

name = input('Enter your name: ')
num = input('Enter your number: ')

phone_check(name, num)