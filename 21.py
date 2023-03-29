def wrap_string_reverse_order(given_str, width):
    given_str = given_str[::-1].replace(' ', '')
    print(given_str)
    wrapped_str = '\n'.join([given_str[i:i + width] for i in range(0, len(given_str), width)])
    print(wrapped_str)
    wrapped_str = wrapped_str[::-1]
    print(wrapped_str)
    return wrapped_str


input_str = input("enter string: ")
wid = int(input("enter width: "))
A = wrap_string_reverse_order(input_str, wid)
