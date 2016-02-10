class board_game:
     def __init__(self, matrix = [], matrix_val = [] , matrix_moves = [], player = 'X'):
         self.matrix = matrix
         self.matrix_val = matrix_val
         self.matrix_moves = matrix_moves
         self.player = player

#Sneak step:-
def adj(mat, row, col, player): #Getting for player = X
    p = mat[row][col]
    #print p
    if mat[row][col] == 'O' or mat[row][col] == 'X':
        return 0
    elif row == 0 and col == 0:                                         #(0,0)
        if (mat[row+1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif row == 4 and col == 0:                                         #(4,0)
        if (mat[row-1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif row == 4 and col == 4:                                         #(4,4)
        if (mat[row-1][col] != player and mat[row][col-1] != player):
            return game.matrix_val[row][col]
    elif row == 0 and col == 4:                                         #(0,4)
        if (mat[row][col-1] != player and mat[row+1][col] != player):
            return game.matrix_val[row][col]
    elif 0 < row < 4 and col == 0:                                      # Left Column
        if (mat[row-1][col] != player and mat[row+1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif 0 < col < 4 and row == 0:                                      # Top Row
        if (mat[row][col-1] != player and mat[row+1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif 0 < col < 4 and row == 4:                                      # Bottom Row
        if (mat[row][col-1] != player and mat[row-1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    elif col == 4 and 0 < row < 4:                                      # Right Column
        if (mat[row][col-1] != player and mat[row+1][col] != player and mat[row-1][col] != player):
            return game.matrix_val[row][col]
    else:                                                               # Middle Elements
        if (mat[row][col-1] != player and mat[row-1][col] != player and mat[row+1][col] != player and mat[row][col+1] != player):
            return game.matrix_val[row][col]
    return 0

#Raid step:-
def raidMove(game, row, col, player):
    maxRaidSum = 0
    #maxRaidSum = game.matrix_val[row][col]
    # max_sum_cur = 0 left_idx = None right_idx = None
    if game.matrix_moves[row][col] == '*':
        if row == 0 and col == 0:                                         #(0,0)
            if game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col+1] == 'O':
                    maxRaidSum += game.matrix_val[row][col+1]
            elif game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row+1][col] == 'O':
                    maxRaidSum += game.matrix_val[row+1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif row == 4 and col == 0:                                         #(4,0)
            if game.matrix_moves[row-1][col] == player:
                if game.matrix_moves[row][col+1] == 'O':
                    maxRaidSum += game.matrix_val[row][col+1]
            elif game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row-1][col] == 'O':
                    maxRaidSum += game.matrix_val[row-1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif row == 4 and col == 4:                                         #(4,4)
            if game.matrix_moves[row-1][col] == player:
                if game.matrix_moves[row][col-1] == 'O':
                    maxRaidSum += game.matrix_val[row][col-1]
            elif game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row-1][col] == 'O':
                    maxRaidSum += game.matrix_val[row-1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif row == 0 and col == 4:                                         #(0,4)
            if game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col-1] == 'O':
                    maxRaidSum += game.matrix_val[row][col-1]
            elif game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row+1][col] == 'O':
                    maxRaidSum += game.matrix_val[row+1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif 0 < row < 4 and col == 0:                                      # Left Column
            if game.matrix_moves[row-1][col] == player or game.matrix_moves[row+1][col] == player or game.matrix_moves[row][col+1] == player:
                if game.matrix_moves[row-1][col] == 'O':
                    maxRaidSum += game.matrix_val[row-1][col]
                if game.matrix_moves[row+1][col] == 'O':
                    maxRaidSum += game.matrix_val[row+1][col]
                if game.matrix_moves[row][col+1] == 'O':
                    maxRaidSum += game.matrix_val[row][col+1]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif 0 < col < 4 and row == 0:                                      # Top Row
            if game.matrix_moves[row][col-1] == player or game.matrix_moves[row][col+1] == player or game.matrix_moves[row+1][col] == player:
                if game.matrix_moves[row][col-1] == 'O':
                    maxRaidSum += game.matrix_val[row][col-1]
                if game.matrix_moves[row][col+1] == 'O':
                    maxRaidSum += game.matrix_val[row][col+1]
                if game.matrix_moves[row+1][col] == 'O':
                    maxRaidSum += game.matrix_val[row+1][col]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif 0 < col < 4 and row == 4:                                      # Bottom Row
            if game.matrix_moves[row][col+1] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row][col+1] == 'O':
                    maxRaidSum += game.matrix_val[row+1][col]
                if game.matrix_moves[row-1][col] == 'O':
                    maxRaidSum += game.matrix_val[row-1][col]
                if game.matrix_moves[row][col-1] == 'O':
                    maxRaidSum += game.matrix_val[row][col-1]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        elif col == 4 and 0 < row < 4:                                      # Right Column
            if game.matrix_moves[row+1][col] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row][col-1] == player:
                if game.matrix_moves[row+1][col] == 'O':
                    maxRaidSum += game.matrix_val[row+1][col]
                if game.matrix_moves[row-1][col] == 'O':
                    maxRaidSum += game.matrix_val[row-1][col]
                if game.matrix_moves[row][col-1] == 'O':
                    maxRaidSum += game.matrix_val[row][col-1]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
        else:                                                               # Middle Elements
            if (game.matrix_moves[row][col-1] == player or game.matrix_moves[row-1][col] == player or game.matrix_moves[row+1][col] == player or game.matrix_moves[row][col+1] == player):
                if game.matrix_moves[row][col-1] == 'O':
                    maxRaidSum += game.matrix_val[row][col-1]
                if game.matrix_moves[row-1][col] == 'O':
                    maxRaidSum += game.matrix_val[row-1][col]
                if game.matrix_moves[row+1][col] == 'O':
                    maxRaidSum += game.matrix_val[row+1][col]
                if game.matrix_moves[row][col+1] == 'O':
                    maxRaidSum += game.matrix_val[row][col+1]
            maxRaidSum = 2*maxRaidSum
            maxRaidSum += game.matrix_val[row][col]
            return maxRaidSum
    return 0

def getPlayerSum(game):
    playersum = 0
    oppPlayerSum = 0
    for value in range(len(game.matrix_moves)):
        for v in range(len(game.matrix_moves[value])):
            if game.matrix_moves[value][v] == 'X': #player
                playersum += game.matrix_val[value][v]
            elif game.matrix_moves[value][v] == 'O': #Opp_player
                oppPlayerSum += game.matrix_val[value][v]
    return playersum, oppPlayerSum


def print_output(game,left_idx,right_idx, flag):
    m = game.matrix_moves
    text_file = open("output.txt","w")
    if flag == 0:
        for i in range(5):
            for j in range(5):
                if i+1 == left_idx and j == right_idx and m[i][j] == "O":
                    text_file.write(game.player)
                elif i == left_idx and j+1 == right_idx and m[i][j] == "O":
                    text_file.write(game.player)
                elif i == left_idx and j-1 == right_idx and m[i][j] == "O":
                    text_file.write(game.player)
                elif i-1 == left_idx and j == right_idx and m[i][j] == "O":
                    text_file.write(game.player)
                elif i == left_idx and j == right_idx:
                    text_file.write(game.player)
                else:
                    text_file.write(m[i][j])
            text_file.write("\n")
    else:
        game.matrix_moves[left_idx][right_idx] = game.player
        for i in range(0,5):
            for j in range(0,5):
                text_file.write(game.matrix_moves[i][j])
            text_file.write("\n")

def GreedyBestFirst(game):
    raidSum = 0
    left_idx = None
    right_idx = None
    for row in range(len(game.matrix_val)):
        for col in range(len(game.matrix_val)):
            #if maxSum < game.matrix_val[row][col]:
            #temp = game.matrix_val[row][col]
            sneak_Sum = adj(game.matrix_moves, row, col, game.player)
            rsum= raidMove(game, row, col,game.player)
            print rsum
            print sneak_Sum
            flag = 0
            if sneak_Sum < rsum:
                if raidSum < rsum:
                    raidSum = rsum
                    left_idx = row
                    right_idx = col
                    flag = 0 # Raid Move
            else:
                if raidSum < sneak_Sum:
                    raidSum = sneak_Sum
                    left_idx = row
                    right_idx = col
                    flag = 1 # Sneak Move
            #outPrint(game,left_idx,right_idx,game.player)
            playerSum, oppPlayerSum = getPlayerSum(game)
            if flag == 1 and left_idx is not None and right_idx is not None:
                e = playerSum - oppPlayerSum
            elif flag == 0 and left_idx is not None and right_idx is not None:
                te = raidSum - game.matrix_val[left_idx][right_idx]
                e = playerSum - 2*te
    print 'Raid Sum'
    print raidSum
    print 'row and column:'
    print left_idx
    print right_idx
    print game.matrix_val[left_idx][right_idx]
    print_output(game,left_idx,right_idx, flag)
    #resMatrix, playerSum, oppPlayerSum = outPrint(game,left_idx,right_idx,game.player, flag)
    print 'Player sum:'
    print playerSum
    print 'opponent player sum:'
    print oppPlayerSum


##def minMaxAlgo(game):



if __name__ == '__main__':
    game = board_game()
    text_file = open("next_state.txt", "r")
    lines = text_file.readlines()

    for line in lines:
        number_strings = line.split()
        numbers = [n for n in number_strings]
        game.matrix.append(numbers)
    print game.matrix

    s = 0
    i = 0
    j = 0

    for value in range(3, len(game.matrix)-5):
        game.matrix_val.append([])
        for v in range(len(game.matrix[value])):
            temp = game.matrix[value][v]
            t = int(temp)
            game.matrix_val[i].append(t)
            if s < t:
                s = t
            j += 1
        i += 1

    j = 0
    for value in range(len(game.matrix)-5,len(game.matrix)):
        game.matrix_moves.append([])
        for v in range(len(game.matrix[value])):
            for x in range(len(game.matrix[value][v])):
                game.matrix_moves[j].append(game.matrix[value][v][x])
        j += 1
    print 'Values:'
    print game.matrix_val
    print 'Moves: '
    print game.matrix_moves
    if game.matrix[2][0] == '1':
        print 'Greedy play'
        GreedyBestFirst(game)
    elif game.matrix[2][0] == 2:
        print 'MinMax play'
        ##minMaxAlgo(game)
    text_file.close()