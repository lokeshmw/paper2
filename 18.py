n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()
