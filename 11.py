def reverse_vowel(str_):
    vowels = set('aeiouAEIOU')
    str_ = list(str_)
    i, j = 0, len(str_) - 1
    while i < j:
        if str_[i] in vowels and str_[j] in vowels:
            str_[i], str_[j] = str_[j], str_[i]
            i += 1
            j -= 1
        elif str_[i] in vowels:
            j -= 1
        elif str_[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1
    return ''.join(str_)


given_string = input("enter a word: ")
A = reverse_vowel(given_string)
print(A)
