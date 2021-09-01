import heapq
import math
import itertools
#from python heapq documentation
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


def path_finder(area):
    global pq, entry_finder, REMOVED
    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'  
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    prev = {}
    dist = {}
    formatted = [list(x) for x in area.split('\n')]
    size = len(formatted)
    for row in range(size):
        for col in range(size):
            dist[(row,col)] = math.inf
            add_task((row,col),math.inf)
    remove_task((0,0))
    add_task((0,0),0)
    dist[(0,0)] = 0
    pos = (0,0)
    while len(pq)!=0:
        try:
            pos =pop_task()
        except KeyError:
            break
        for move in moves:
            if(pos[0]+move[0]<size and pos[0]+move[0]>=0 and
               pos[1]+move[1]<size and pos[1]+move[1]>=0):
                next = (pos[0]+move[0],pos[1]+move[1])
                newdist = dist[pos]+abs(int(formatted[next[0]][next[1]])-int(formatted[pos[0]][pos[1]]))
                if(newdist<dist[next]):
                    dist[next] = newdist
                    prev[next] = pos
                    remove_task(next)
                    add_task(next,newdist)
    
    return dist[(size-1,size-1)]
