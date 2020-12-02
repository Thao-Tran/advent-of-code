import fileinput
freq = 0
for line in fileinput.input("day1.txt"):
    freq += int(line)

print(freq)
