def dispatch_if(operator, x , y):

    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y


def dispatch_if_dict(operator, x, y):

    func_dict =  {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }
    return func_dict.get(operator, lambda: None)()



print(dispatch_if('mul', 2, 5))
print(dispatch_if_dict('mul', 2, 5))
