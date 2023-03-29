def count_ones(n):
    count = 0
    for i in range(n + 1):
        count += str(i).count('1')
    return count


num_ = int(input("enter:"))
print(count_ones(num_))
