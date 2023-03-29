n = 3
simulated_values = ['CCRLU', 'CRLCUC', 'CCCC']
for values in simulated_values:
    num_chairs = 0
    waiting_employees = 0
    for val in values:
        if val == 'C':
            if waiting_employees > 0:
                waiting_employees -= 1
        else:
            num_chairs += 1
            elif val == 'R' or val == 'L':
            num_chairs -= 1
        elif val == 'U':
            if num_chairs > 0:
                num_chairs -= 1
        else:
            waiting_employees += 1
        print(waiting_employees + num_chairs)