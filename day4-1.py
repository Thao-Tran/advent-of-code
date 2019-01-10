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
topGuard = 0
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

    if guard not in guardSleep:
        guardSleep[guard] = 0

    for minute in range(sortedActions[timeInd].minute,
                        sortedActions[timeInd + 1].minute + 1):
        if minute not in guardMinutes[guard]:
            guardMinutes[guard][minute] = 0

        guardMinutes[guard][minute] += 1
        guardSleep[guard] += 1

    if topGuard in guardSleep and guardSleep[guard] < guardSleep[topGuard]:
        continue

    topGuard = guard

topMinute = 0
for minute in range(0, 59):
    if minute in guardMinutes[topGuard] and guardMinutes[topGuard][
            minute] > guardMinutes[topGuard][topMinute]:
        topMinute = minute

print "Guard " + str(topGuard) + " slept " + str(
    guardSleep[topGuard]) + " minutes and was asleep during minute " + str(
        topMinute) + " the most (" + str(
            guardMinutes[topGuard][topMinute]) + " days)"
