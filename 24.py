str1 = input("enter input: ")
word = input("enter input: ")
combinations = set()
left = 0
right = len(word) - 1
while right < len(str1):
    x = str1[left:right+1]
    if sorted(x) == sorted(word):
        combinations.add(x)
    left += 1
    right += 1
print(combinations)
