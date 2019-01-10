import fileinput
freqs = [0]
freq = 0
repeated = False
while not repeated:
    for line in fileinput.input("day1.txt"):
        freq = freqs[len(freqs)-1] + int(line)
        if freqs.count(freq) > 0:
            print("repeated")
            repeated = True
            break
        freqs.append(freq)
print(freq)
