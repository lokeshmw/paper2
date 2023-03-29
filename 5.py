given_dict = {"Msys Technologies": "Sanjay Sehgal", "Infosys": "Salil Parekh",
              "TCS": "Rajesh Gopinathan", "Wipro": "Thierry Delaporte"}
values_ = []
for i in given_dict:
    values_.append(given_dict[i])
    values_.sort()

print(values_)
