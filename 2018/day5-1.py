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
print len(polymer), len(splitPolymer(polymer))
