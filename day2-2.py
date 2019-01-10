import fileinput
d = []
boxNum = 0
for boxID in fileinput.input("day2.txt"):
    charMatches = []
    for charInd in range(0, len(boxID)):
        if len(d) < len(boxID):
            d.append([])
        else:
            box = 0
            matches = []
            for char in d[charInd]:
                if char == boxID[charInd]:
                    matches.append(box)
                box += 1

            charMatches.append(matches)

        d[charInd].append(boxID[charInd])

    if len(charMatches) < len(boxID) - 1:
        boxNum += 1
        continue

    charDiffer = -1
    for charInd in range(0, len(charMatches)):
        for box in charMatches[charInd]:
            charDiffer = -1
            for ind in range(0, len(charMatches)):
                if charInd != ind and charMatches[ind].count(box) == 0:
                    if charDiffer != -1:
                        charDiffer = -1
                        break
                    charDiffer = ind
            if charDiffer != -1:
                break
        if charDiffer != -1:
            print(boxID[:charDiffer-1] + boxID[charDiffer+1:])
            break

    if charDiffer != -1:
        break
    boxNum += 1
