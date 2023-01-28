import random


def evaluate(boardgame):
    """Evaluates the status of the game"""
    if "xxx" in boardgame:
        return "x"
    elif "ooo" in boardgame:
        return "o"
    elif "-" not in boardgame:
        return "!" 
    else:
        return "-"                 

def move(boardgame, mark, position):
    """Returns the board with the specified mark placed in the specified position"""
    updatedboard=boardgame[:position] + mark + boardgame[position+1:]
    return updatedboard
    
def player_move(boardgame, mark1):
    position=int(input("which position do you play?"))
    while position>=20 or position<0:
        print("select a position between 0-19!")
        position=int(input("which position do you play?"))
    if boardgame[position] != "-":
        print("The position you selected is occupied. Select a new position!")
        position=int(input("which position do you play?"))
        return move(boardgame, mark1, position)
    else:
        return move(boardgame,mark1, position)


def pc_move(boardgame, mark2):
    pc_position=random.randint(0,19)
    while boardgame[pc_position] != "-":
        pc_position=random.randint(0,19)
    else:
        return move(boardgame,mark2,pc_position)    


def tictactoe_1D():
    """Creates an empty board and lets the user play against the computer until the game is finished"""
    board = "--------------------"
    print("Let's play a game of tic-tac-toe!")
    
    while True:
        player_mark = input("which mark do you select, x or o? ")
        if player_mark != "x" and player_mark != "o":
            print("you can select only x or o")
            continue    
        else:
            break
    if player_mark =="x":
        pc_mark="o"
    elif player_mark=="o":
        pc_mark="x"
    print("The PC mark will be: ", pc_mark)    
    print("starting board", board)

    while evaluate(board)=="-":
        board1=player_move(board, player_mark)
        print(board1)
        board2=pc_move(board1, pc_mark) 
        print(board2)
        evaluate(board2)
        board=board2  #updating the board after every round
        if evaluate(board)=="x":
            if player_mark == "x":
                print("You won!")
            elif player_mark=="o":
                print("the computer won!")
        elif evaluate(board)=="o":
            if player_mark=="o":
                print("You won!") 
            else:
                print("the computer won!")     
        elif evaluate(board)=="!":
            print("its a draw!")     

tictactoe_1D()        