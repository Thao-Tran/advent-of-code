import re
puzzleInput = open("day3.txt").read().strip().replace(" ", "").split("\n")
puzzleInput = {re.sub(r"#|@.+","",line):[int(v) for v in re.split(r",|:|x", re.sub(r"\A(#\d+@)", "", line))] for line in puzzleInput}
inchesUsed = 0
fabric = {}
for boxID, box in puzzleInput.items():
    left, top, width, height = box
    for x in range(left+1, left+width+1):
        for y in range(top+1, top+height+1):
            coord = str(x)+","+str(y) 
            if coord not in fabric.keys():
                fabric[coord] = 0
            fabric[coord] += 1
for boxID, box in puzzleInput.items():
    left, top, width, height = box
    overlap = False
    for x in range(left+1, left+width+1):
        for y in range(top+1, top+height+1):
            coord = str(x)+","+str(y) 
            if fabric[coord] > 1:
                overlap = True
                break
        if overlap:
            break
    if not overlap:
        print(boxID)
