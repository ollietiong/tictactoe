board = [["EMPTY", "EMPTY", "X"],
            ["EMPTY", "X", "EMPTY"],
            ["X","EMPTY", "EMPTY"]]



# there are only 2 winning positions
# only need to check board[0][0] and board [0][2]

center_point = board[1][1]
if center_point == "X" or center_point == "O":
    if (board[0][0] == center_point and board[2][2] == center_point) or (board[0][2] == center_point and board[2][0]):
        print(center_point + " win")
     
    