from functools import reduce
l_list = [1, 2, 3, 4, 5, 6, 7]
max = reduce(lambda x, y: x if (x > y) else y, l_list)
print(max)
