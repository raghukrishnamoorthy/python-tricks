xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)

import copy
ys = copy.copy(xs) #shallow copy
ys = copy.deepcopy(xs) #deep copy

