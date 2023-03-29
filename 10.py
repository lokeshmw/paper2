given_String  = "MsYs TecHNOlogiEs iS a gREat place To woRk"
count_lower = 0
count_upper = 0
for each_char in given_String:
    if each_char.islower():
        count_lower += 1
    elif each_char.isupper():
        count_upper += 1

print("upper= ", count_upper)
print("lower= ", count_lower)