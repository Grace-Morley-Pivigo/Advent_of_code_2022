file = open("imput_1.txt", "r")
lines = file.readlines()
lines = [i.replace("\n", "") for i in lines]

totals = []
total = 0
for line in lines:
    if line == "":
        totals.append(total)
        total = 0
    else:
        total += int(line)

totals.sort(reverse=True)
print(sum(totals[0:3]))
