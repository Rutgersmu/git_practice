in_file = open('chicken.txt', 'r')
rev = 0
day = 0
for line in in_file:
    data = line.strip().split(": ")
    amount = int(data[1])
    rev += amount
    day += 1

ave_rev = rev / day
print(ave_rev)

in_file.close()

print(chanmu)
print(question)