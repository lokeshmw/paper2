input_string = input("Enter a string: ")
words = input_string.split()
palindromes = {}
for i in words:
	i = ''.join(e for e in i if e.isalnum()).lower()
	if i == i[::-1]:
		palindromes[i] = palindromes.get(i, 0) + 1
print(palindromes)
