A = int(input("Enter a positive number: "))
rev_A = 0
while A > 0:
    reminder = A % 10
    rev_A = rev_A * 10 + reminder
    A = A//10

print(rev_A)
