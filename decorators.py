#decorators are used to add something before and after function

def my_decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")
    
    return wrapper


@my_decorator
def hello():
    print("Hello Noor")


hello()

#decorator as function argument
def my_decorator(function):
    def wrapper(name):
        print("Starting...")
        function(name)
        print("Finished...")
    
    return wrapper


@my_decorator
def greet(name):
    print("Hello", name)


greet("Noor")

#decorator for checking age 
def check_age(function):
    def wrapper(age):
        if age >= 18:
            function(age)
        else:
            print("You are not eligible")
    
    return wrapper


@check_age
def vote(age):
    print("You can vote")


vote(20)
vote(16)

