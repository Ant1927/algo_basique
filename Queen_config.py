def queen_placement(chessboard,pos_x,pos_y):
    for i in range(len(chessboard)):
        for j in range(len(chessboard)):
            if chessboard[pos_x][j] == 1:
                return False
            if abs(pos_y-j)==abs(pos_x-i):
                if chessboard[i][j]==1:
                    return False
        if chessboard[i][pos_y]==1:
            return False
    return True

def back_track(crt_chessboard,nbr_queen_2_place,column):
    global found_config,iter
    sol_pos = True
    if nbr_queen_2_place==0:
        found_config += 1
        return False
    for i in range(len(crt_chessboard)):
        sol_pos=True
        if queen_placement(crt_chessboard,i,column):
            crt_chessboard[i][column]=1
            nbr_queen_2_place-=1
            sol_pos = back_track(crt_chessboard,nbr_queen_2_place,column+1)
            if sol_pos == False :
                crt_chessboard[i][column]=0
                nbr_queen_2_place += 1
            iter+=1
    return False

global found_config,iter
iter=0
n=10
empty_chessboard = [[0 for i in range(n)] for j in range(n)]
found_config = 0
back_track(empty_chessboard,n,0)
print(found_config,iter)
