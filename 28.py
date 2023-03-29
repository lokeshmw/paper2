def reverse_str(given_str, k):
    s_list = list(given_str)
    for i in range(0, len(given_str), 2 * k):
        left = i
        right = min(i + k - 1, len(given_str) - 1)
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return ''.join(s_list)


str_ = input('enter a string: ')
num = int(input("enter: "))
print(reverse_str(str_, num))
