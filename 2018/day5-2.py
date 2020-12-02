def splitPolymer(polymer):
    if len(polymer) == 1:
        return polymer
    elif len(polymer) == 2:
        if abs(ord(polymer[0]) - ord(polymer[1])) == 32:
            return ""
        return polymer

    left = splitPolymer(polymer[:len(polymer) / 2])
    right = splitPolymer(polymer[len(polymer) / 2:])
    while len(left) > 0 and len(right) > 0 and abs(
            ord(left[len(left) - 1]) - ord(right[0])) == 32:
        left = left[:len(left) - 1]
        right = right[1:]

    return left + right


polymer = open("day5.txt").read().strip().replace(" ", "")

smallestPolymer = -1

for charNum in range(ord('A'), ord('Z') + 1):
    polymerLength = len(
        splitPolymer(
            polymer.replace(chr(charNum), "").replace(chr(charNum + 32), "")))
    if smallestPolymer == -1 or polymerLength < smallestPolymer:
        smallestPolymer = polymerLength

print smallestPolymer
