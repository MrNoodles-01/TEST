# TEST
TESTING 123


weight_list_first = []
name_list = []
diff_list = []
count = 0

for i in range(3):
    name = input("Input name of student - ")
    name_list.append(name)
    weightA = float(input("Input weight of " + name + " (in kg) on the first day of the term - "))
    while 30 > weightA or weightA > 110:
        print("Invalid weight, please re-enter.")
        weightA = float(input("Re-enter weight of " + name + " (in kg) - "))
    if 30 <= weightA <= 110:
        weight_list_first.append(weightA)
    weightB = float(input("Input weight of " + name_list[count] + " (in kg) on the last day of the term - "))
    while 20 > weightB or weightB > 120:
        print("Invalid weight, please re-enter.")
        weightB = float(input("Re-enter weight of " + name_list[count] + " (in kg) - "))
    if 30 <= weightB <= 110:
        diff_list.append((weight_list_first[count] - weightB) * -1)
    count += 1

count = 0

for k in range(3):
    if diff_list[count] > 2.5:
        print(str(name_list[count]) + " has gained more that 2.5 kg.")
    elif diff_list[count] < -2.5:
        print(str(name_list[count]) + " has lost more than 2.5 kg.")
    count += 1
