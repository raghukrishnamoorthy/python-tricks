def print_vector(x, y, z):
    print("<%s %s %s>" % (x, y, z))

tuple_vec = (1, 2, 3)
dict_vec = {'x': 1, 'y': 2, 'z': 3}
print_vector(*tuple_vec)
print_vector(**dict_vec)