list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]
new_list = list(filter(lambda x: x % 2 == 0 or x % 5 == 0, list_1))
print(new_list)
