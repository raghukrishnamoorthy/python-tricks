add = lambda x, y: x + y

tuples = [(1, 'd'), (2, 'c'), (3, 'd'), (4, 'e')]
print(sorted(tuples, key = lambda x: x[1]))

print(add(5, 10))

print(sorted(range(-5, 6), key = lambda x: x * x))

def make_adder(n):
    return lambda x: x + n


plus_3 = make_adder(3)
print(plus_3(5))