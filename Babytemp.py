
temprange = []
timemin = 0
count = 0
avtemp = 0
unsuitabletemp = 0
tempmin = 100
tempmax = 0

while timemin <= 180:
    temprange.append(float(input("Temperature (degrees celcius) " + str(timemin) + " min -")))
    timemin += 10
    if temprange[count] < 36 or temprange[count] > 37.5:
        unsuitabletemp += 1
    if unsuitabletemp >= 2:
        break


count = 0

for i in range(len(temprange)):
    avtemp = avtemp + temprange[count]
    count += 1

avtemp = avtemp / len(temprange)

if unsuitabletemp >= 2:
    print("Warning baby/'s temparature is out of range!")
elif avtemp < 36:
    print("Baby's temperature is too low!")
    print("Average temperature (degrees celcius) = " + str(avtemp))
elif avtemp > 37.5:
    print("Baby's temperature is too high!")
    print("Average temperature (degrees celcius) = " + str(avtemp))
else:
    print("Baby's temparature is good.")
    print("Average temperature (degrees celcius) = " + str(avtemp))

print(temprange)

