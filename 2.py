A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
New_A = []
for i in A:
    if i % 2 == 0:
        New_A.append(i**2)
    else:
        New_A.append(i ** 3)
print(New_A)