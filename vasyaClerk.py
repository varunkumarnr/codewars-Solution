def tickets(people):
    price = 25
    charge = {
        25: 0,
        50: 0,
        100: 0,
    }
    for i in range(len(people)):
        if people[i] == price:
            charge[people[i]] += 1
        else:
            charge[people[i]] += 1
        if people[i] == 50 and charge[25] < 1:
            print("no")
            return "NO"
        elif people[i] == 50:
            charge[25] -= 1
        if people[i] == 100 and charge[25] < 3 and (charge[50] < 1 or charge[25] < 1):
            print("no")
            return "NO"
        elif people[i] == 100:
            if charge[25] > 3:
                charge[25] -= 3
            elif charge[50] > 1 and charge[25] > 1:
                charge[25] -= 1
                charge[50] -= 1
    print("y")
    return "YES"


tickets([25, 25, 25, 100, 25, 25, 25, 100, 25, 25, 50, 100, 25, 25, 50, 100, 50, 50])
