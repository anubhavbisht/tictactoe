board=['-','-','-','-','-','-','-','-','-']
condition=True
positions=list()
## to display a board
## 1|2|3
## 4|5|6
## 7|8|9
## here 1 to 9 suggests position in tic tac toe board
def diplay_board():
  print(board[0]+"|"+board[1]+'|'+board[2])
  print(board[3]+"|"+board[4]+'|'+board[5])
  print(board[6]+"|"+board[7]+'|'+board[8])

def checkoutcome(player,weapon):
    ##global keyword is used to change the value of variable condition
    global condition
    ##to check row wise
    if (board[0]==board[1]==board[2]==weapon) or (board[3]==board[4]==board[5]==weapon) or (board[6]==board[7]==board[8]==weapon):
        condition=False
        print("{} wins".format(player))
    ## to check column wise
    elif (board[0]==board[3]==board[6]==weapon) or (board[1]==board[4]==board[7]==weapon) or (board[2]==board[5]==board[8]==weapon):
        condition=False
        print("{} wins".format(player))
    ##to check diagonally
    elif (board[0]==board[4]==board[8]==weapon) or (board[2]==board[4]==board[6]==weapon):
        condition=False
        print("{} wins".format(player))
    ##nothing yet
    else:
        pass
def handleturn(player,weapon):
    ##taking input from players for where to put their weapon in board
    ## -1 is done in position as list indexing starts from 0
    position=int(input("choose a position from 1 to 9 {}::".format(player)))-1
    ##if user does not give justied position
    while position not in [0,1,2,3,4,5,6,7,8]:
        print("you have entered invalid position") 
        position=int(input("choose a position from 1 to 9 {}::".format(player)))-1
    ##if user actually puts his weapon in already acquired position
    while (position in positions):
        print("that position is already taken by you or by your rival")
        diplay_board()
        position=int(input("choose a position from 1 to 9 {}::".format(player)))-1
    ##putting at that position
    board[position]=weapon
    checkoutcome(player,weapon)
    ##to keep hold of all the positions
    positions.append(position)
    diplay_board()
def playgame():
    count=0
    print("this is a game of tic tac toe")
    print("tic tac toe boards looks like")
    diplay_board()
    ## taking inputs from users
    ##here weapon means X or O or you can use anything
    player1,weapon1=input("enter player1 name and weapon::").split()
    player2,weapon2=input("enter player2 name and weapon::").split()
    ##to keep hold of number of chances
    while(count<=8 and condition==True):
        ##to flip turns from user1 to user2
        if count%2==0:
            handleturn(player1,weapon1)
        else:
            handleturn(player2,weapon2)
        count+=1
    ##if no winner or loser
    if count==9 and condition==True:
        print("game is tied")
##to start the game initially
playgame()

