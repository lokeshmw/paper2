dict1 = {'name': 'Msys', 'Place': 'Pune'}
dict2 = {'EmpID': 3285, 'Salary': 50000}
merged_dict = {**dict1, **dict2}
print(merged_dict)

merged_dict['salary'] *= 1.1

merged_dict['age'] = 35

keys = tuple(merged_dict.keys())
values = tuple(merged_dict.values())
print(keys)
print(values)

del merged_dict['age']
print(merged_dict)
