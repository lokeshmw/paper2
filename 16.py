input_str = "Hello World"
input_str = input_str.split()
print(input_str)
for word in input_str:
    print(word[::-1], end=' ')
