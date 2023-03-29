A = ['Nissan', "maruti", "hyundai", "Volkswagen", "audi"]
B = []
for i in A:
    if i[0].islower():
        B.append(i)

print(B)

