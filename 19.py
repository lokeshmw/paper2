def remove_char(given_str, cha):
    if cha not in given_str:
        raise Exception("Given character is not present in the string. Please try with a new one")
    return given_str.replace(cha, "")


given_string = input("Enter a string: ")
i = input("Enter a character to remove: ")

try:
    new_string = remove_char(given_string, i)
    print("New string:", new_string)
except Exception as e:
    print(e)
