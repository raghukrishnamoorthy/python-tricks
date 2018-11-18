xs = {
    'a': 1,
    'b': 2
}

ys = {
    'b': 3,
    'c': 4
}

zs = {}
zs.update(xs)
zs.update(ys)
print(zs)
zs = dict(xs, **ys)
print(zs)
zs = {**xs, **ys}
print(zs)