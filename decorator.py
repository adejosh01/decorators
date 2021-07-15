import functools

def school(func):
    """Print the function """
    def wrapper(*args, **kwargs):
        print("Welcome to my {} ".format(func.__name__))
        return func(*args , **kwargs)
    return wrapper


@school
def School(name, location):
    print('The name of my school is {} located at {}'.format(name, location))

name = input("Enter your name of your school here ")
location = input("Enter your location ")
School(name, location)