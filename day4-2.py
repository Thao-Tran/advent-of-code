from datetime import datetime as d
from datetime import timedelta
import re

records = re.sub(r"^\s|\s$", "", open("day4.txt").read()).split("\n")
shiftTimes = {
    d.strptime(re.sub(r"(^\s)|\[|(\].+)|(\s$)", "", rec), "%Y-%m-%d %H:%M"):
    int(re.sub(r"\[.+\]|\D", "", rec))
    for rec in records if "Guard" in rec
}
actionTimes = {
    d.strptime(re.sub(r"(^\s)|\[|(\].+)|(\s$)", "", rec), "%Y-%m-%d %H:%M"):
    re.sub(r"(\[[^a-z]+)|(\]\s+)", "", rec)
    for rec in records if "Guard" not in rec
}

guardSleep = {}
guardMinutes = {}
guardInd = 0
sortedShifts = shiftTimes.keys()
sortedShifts.sort()
sortedActions = actionTimes.keys()
sortedActions.sort()

for timeInd in range(0, len(sortedActions), 2):
    while guardInd < len(sortedShifts) - 1\
            and sortedActions[timeInd] >= sortedShifts[guardInd + 1]:
        guardInd += 1

    guard = shiftTimes[sortedShifts[guardInd]]

    if guard not in guardMinutes:
        guardMinutes[guard] = {}

    for minute in range(sortedActions[timeInd].minute,
                        sortedActions[timeInd + 1].minute):
        if minute not in guardMinutes[guard]:
            guardMinutes[guard][minute] = 0

        guardMinutes[guard][minute] += 1

sortedGuards = guardMinutes.keys()
sortedGuards.sort()

topGuard = sortedGuards[0]
topMinute = guardMinutes[topGuard].keys()[0]
for guard in sortedGuards:
    for minute in guardMinutes[guard]:
        if guardMinutes[guard][minute] >= guardMinutes[topGuard][topMinute]:
            topGuard = guard
            topMinute = minute

print "Guard " + str(topGuard) + " minute " + str(topMinute)
print topGuard * topMinute
