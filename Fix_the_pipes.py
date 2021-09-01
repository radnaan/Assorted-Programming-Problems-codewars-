def check_pipe(pipe_map):
    rows = len(pipe_map)
    cols = len(pipe_map[0])
    for y  in range(rows):
        if(not DFS(pipe_map,(y,0)) or  not DFS(pipe_map,(y,cols-1))):
            return False

    for x  in range(cols):
        if(not DFS(pipe_map,(0,x)) or  not DFS(pipe_map,(rows-1,x))):
            return False
    return True

def DFS(maze,start):
    pipes = {'┗':[(-1,0),(0,1)],'┓':[(1,0),(0,-1)],'┏':[(1,0),(0,1)],
             '┛':[(-1,0),(0,-1)],'━':[(0,1),(0,-1)],
             '┃':[(1,0),(-1,0)],'┣':[(1,0),(-1,0),(0,1)],'┫':[(1,0),(-1,0),(0,-1)],
             '┳':[(0,1),(0,-1),(1,0)],'┻':[(0,1),(0,-1),(-1,0)],'╋':[(1,0),(-1,0),(0,1),(0,-1)],
            }
    stack = [start]
    explored = {}
    formatted = [list(x) for x in maze]
    sizey = len(formatted)
    sizex = len(formatted[0])
    if(formatted[start[0]][start[1]]=='.'):
        return True
    moves = list(map(lambda x:(start[0]+x[0],start[1]+x[1]), pipes[formatted[start[0]][start[1]]]))
    sources = [(-1,start[1]),(sizey,start[1]),(start[0],-1),(start[0],sizex)]
    intersect = [x for x in sources if x in moves]
    if(len(intersect)==0):
        return True
    while(len(stack)!=0):
        pos = stack.pop(0)
        moves = pipes[formatted[pos[0]][pos[1]]]
        for move in moves:
            if(pos[0]+move[0]<sizey and pos[0]+move[0]>=0 and
               pos[1]+move[1]<sizex and pos[1]+move[1]>=0):
                next = (pos[0]+move[0],pos[1]+move[1])
                if(formatted[next[0]][next[1]]=='.'):
                    return False
                else:
                    othermoves = pipes[formatted[next[0]][next[1]]]
                    if(not pos  in list(map(lambda x:(next[0]+x[0],next[1]+x[1]), othermoves))):
                        return False
                if(next not in explored):
                    stack.append(next)
                    explored[next] = 0

    return True 
