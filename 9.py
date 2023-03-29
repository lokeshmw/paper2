A_list = [1, 2, 1, 5, 9, 10, 2, 2, 7, 5, 3, 10, 8, 9, 15, 17, 21, 16, 17, 90]
len_A_list = len(A_list)
unique = []
for i in A_list:
    if i in unique:
        continue
    else:
        unique.append(i)
print("unique ones: ", unique)
len_unique = len(unique)
print("lenght of unique: ",len_unique)
diff = len_A_list - len_unique
print("difference between the length of the list and the count of unique elements in the list:  ", diff)
