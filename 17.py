def remove_duplicates(string):
    result = []
    for char in string:
        if len(result) == 0 or result[-1] != char:
            result.append(char)
        else:
            result.append('_')
    return ''.join(result)


input_string = 'abcdaa hssbbye'
output_string = remove_duplicates(input_string)
print(output_string)
