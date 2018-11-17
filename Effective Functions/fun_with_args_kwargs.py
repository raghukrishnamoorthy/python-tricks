def foo(required, *args, **kwargs):
    kwargs['temp'] = 'kingon'
    newargs = args + ('extra', )
    print(required)
    if args:
        print(newargs)
    if kwargs:
        print(kwargs)

