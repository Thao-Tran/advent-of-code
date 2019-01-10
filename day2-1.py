import fileinput
twos = 0
threes = 0
for line in fileinput.input("day2.txt"):
    charSet = set(line)
    for letter in charSet:
        if line.count(letter) == 2:
            twos += 1
            break
    for letter in charSet:
        if line.count(letter) == 3:
            threes += 1
            break

print("Checksum: " + str(twos*threes))
