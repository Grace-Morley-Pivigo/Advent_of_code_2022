file = open("imput_1.txt", "r")
lines = file.readlines()
lines = [i.replace("\n", "") for i in lines]

biggest = 0
total = 0
for line in lines:
    if total > biggest:
        biggest = total
    if line == "":
        total = 0
    else:
        total += int(line)

print(biggest)
