import  sys
input_lines = sys.stdin.readlines()
input_lines = [ line.rstrip() for line in input_lines ]
N,M = int(input_lines[0].split(' ')[0]),int(input_lines[0].split(' ')[1])
chess_board = [ line for line in input_lines[1:]]
def select_board(i,j,ch_board) :
    return [ [apb for apb in lne[j:j+8]] for lne in ch_board[i:i+8] ]
def check_chess(board) :
    WB = ['W','B']*4
    BW = ['B','W']*4
    check_board_BW = [BW,WB]*4
    check_board_WB = [WB,BW]*4
    check_BW = 0
    check_WB = 0
    for i in range(8) :
        for j in range(8) :
            if board[i][j] != check_board_BW[i][j] :
                check_BW +=1
            if board[i][j] != check_board_WB[i][j] :
                check_WB +=1
    return min(check_BW,check_WB)

min_check = N*M
for i in range(N-7) :
    for j in range(M-7) :
        now_chess = select_board(i,j,chess_board)
        now_check = check_chess(now_chess)
        min_check = min(now_check,min_check)
print(min_check)
