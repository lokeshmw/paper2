dict1 = {"a": 1, "b": 23}
dict2 = {"c": 3, "d": 43}
print(dict2.update(dict1))
print(dict2)
print({**dict1, **dict2})

