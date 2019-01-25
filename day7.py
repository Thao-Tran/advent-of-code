import re
puzzleInput = [re.sub(r'(^\s)|(\s$)|(Step\s)|(\sm.*p\s)|(\sc.*)', '', line) for line in open('day7.txt').read().strip().split('\n')]
roots = set([step[0] for step in puzzleInput])
steps = set([step[1] for step in puzzleInput])
graph = {root: [] for root in roots}
parents = {step: [] for step in steps}

for step in puzzleInput:
    graph[step[0]] += step[1]
    parents[step[1]] += step[0]
    if step[1] in roots:
        roots.remove(step[1])

def part1():
    available = sorted(roots)
    order = ''
    while len(available) > 0:
        step = available[0]
        if step in graph.keys():
            for branch in graph[step]:
                if branch in parents.keys():
                    parents[branch].remove(step)
                    if len(parents[branch]) == 0:
                        available += branch
                        del parents[branch]
                else:
                    available += branch
        order += step
        available.remove(step)
        available.sort()
    return order

def part2():
    done = ''
    available = []
    workers = {}
    time = 0
    for i in range(len(roots)):
        if i > 4:
            break
        workers[sorted(roots)[i]] = 0

    print workers
    while len(workers.keys()) > 0:
        completed = ''
        minStepTime = 0
        for step, start in workers.items():
            stepTime = start + ord(step) - 4
            if minStepTime == 0 or stepTime < minStepTime:
                minStepTime = stepTime
                completed = step

        time = minStepTime
        done += completed
        del workers[completed]
        if completed in graph.keys():
            for branch in graph[completed]:
                if branch in parents.keys():
                    parents[branch].remove(completed)
                    if len(parents[branch]) == 0:
                        available += branch
                        del parents[branch]
                else:
                    available += branch
        while len(available) > 0 and len(workers.keys()) < 5:
            available.sort()
            workers[available[0]] = time
            del available[0]
        print available, workers

    return (done, time)
