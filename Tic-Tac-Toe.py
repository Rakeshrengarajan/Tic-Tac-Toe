# Tic Tac Toe Game
from IPython.display import clear_output
import random 

# creating board with nine places

def display_board(board):
    clear_output()
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')

# This function is to select the marker for each player

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == "O"):
        marker = input("Enter a Marker X/O for player one : ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker

# To check if a player wins or not. There are 8 possibilities for a player to win.

def win_check(board,marker):
    
    if( (board[7]==marker and board[8]==marker and board[9]==marker) or
        (board[4]==marker and board[5]==marker and board[6]==marker) or
        (board[1]==marker and board[2]==marker and board[3]==marker) or
        (board[7]==marker and board[4]==marker and board[1]==marker) or
        (board[8]==marker and board[5]==marker and board[2]==marker) or
        (board[9]==marker and board[6]==marker and board[3]==marker) or
        (board[7]==marker and board[5]==marker and board[3]==marker) or
        (board[9]==marker and board[5]==marker and board[1]==marker)):
        return True
    else:
        return False

# To tell will player must start first,it will tell randomly



def choose_first():
    num = random.randint(0,1)
    
    if num == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# To check if the position given by the player is empty or not.

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    isFull = True
    for i in board:
        if i == ' ':
            isFull = False
    return isFull

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True   

def players_choice(board):
    position = 0
    
    while not position in [1,2,3,4,5,6,7,8,9] or not space_check(board,position) : 
        position = int(input("Enter your next position : "))
        
    return position


def replay():
    return input("Do you want to play again (Y/N) : ").lower().startswith('y')


# Here Comes the final Assembly of the game 

while True:
    
    board = [' ']* 10
    
    
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    
    print(turn + " Will play First")
    
    play_game = input("Are you ready to play the game Y/N").lower().startswith('y')
    
    if play_game:
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            
            # Game logic starts here for player 1 
            
            display_board(board)
            position = players_choice(board)
            place_marker(board,player1_marker,position)
            
            if win_check(board,player1_marker):
                display_board(board)
                print("Player 1 Won the game! congratulations")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The Game is Draw, Better luck next time !!')
                    break
                else:
                    turn = "Player 2"
        else:
            # Player 2 Logic 
            
            display_board(board)
            position = players_choice(board)
            place_marker(board,player2_marker,position)
            
            if win_check(board,player2_marker):
                display_board(board)
                print("Player 2 Won the game!! congratulations")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The Game is Draw, Better luck next time !!')
                    break
                else:
                    turn = "Player 1"
    
    if not replay():
        break

