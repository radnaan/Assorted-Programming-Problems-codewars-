def formatcoord(coord):
    col = ord(coord[0])-ord('a')
    row = 8- int(coord[1]) 
    return (row,col)

def pawn_move_tracker(moves):
    print(moves)
    board = [
    [".",".",".",".",".",".",".","."],
    ["p","p","p","p","p","p","p","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    ["P","P","P","P","P","P","P","P"],
    [".",".",".",".",".",".",".","."]
    ]
    turn=-1
    piece = {-1:"P", 1:"p"}
    for move in moves:
        if(len(move)==2):
            row, col = formatcoord(move[:2])
            if(board[row][col] != "."):
                return move + " is invalid"
            oldrow = row-turn
            if(board[row-turn][col]=='.'):
                if(((row-turn*2)in (1, 6)) and board[row-turn*2][col]!='.'):
                    oldrow = row-turn*2
                else:
                    return move + " is invalid"                   
            board[oldrow][col] = "."
            board[row][col]=piece[turn]
        elif(len(move)==4):
            row,col = formatcoord(move[2:4])
            offset = ord(move[2])-ord(move[0])
            if(board[row][col] == "." or  board[row-turn][col-offset] == "."):
                return move + " is invalid"
            board[row-turn][col-offset] = "."
            board[row][col]=piece[turn] = piece[turn]                       
        turn = turn * -1
    return board
