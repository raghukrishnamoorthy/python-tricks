import functools

def null_decorator(func):
    print("This is now decorated")
    return func


def uppercase(func):
    
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    
    return wrapper

@uppercase
def greet():
    return "Hello"

print(greet())


def strong(func):
    
    def wrapper():
        return '<strong>' + func() + '</strong>'
    
    return wrapper

def emphasis(func):
    
    def wrapper():
        return '<em>' + func() + '</em>'
    
    return wrapper

@strong
@emphasis
def speaker():
    return("Hello")

speaker()

def proxy(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    return wrapper

def trace(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__} with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: called {func.__name__} with result {original_result}')
        return original_result
    
    return wrapper

@trace
def Add(x, y):
    return x + y

print(Add(5, 7))
print(Add.__name__)