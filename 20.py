def extract_digits(s):
    digits = [c for c in s if c.isdigit()]
    return ''.join(sorted(digits))


def extract_special_chars(s):
    special_chars = set(s) & set('!@#$%^&*()_+-={}|[]\:";\'<>?,./')
    return ''.join(special_chars)


def extract_vowels(s):
    vowels = [c for c in s if c.lower() in 'aeiou']
    return ''.join(reversed(vowels))


s = input("enter a random string : ")
print("Input string:", s)
print("Digits:", extract_digits(s))
print("Special characters:", extract_special_chars(s))
print("Vowels:", extract_vowels(s))
