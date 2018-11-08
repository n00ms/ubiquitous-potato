#warning this code was made by beginners and any small changes will result in poor execution/ multiple errors
import random

def display(): #prints column numbers
    i = 1
    while i <= 6:
        if i == 6:
            print ((" "*9), i, sep="")
            i += 1
        else:
            print ((" "*9), i, sep="", end="")
            i += 1

    num = 1
    i = 1
    while i <= 60:
        if i == 60:
            num = 0
            print (num,sep="")
        elif num == 10:
            num = 0
            print (num,end="")
        else:
            print (num,end="")
        num += 1
        i += 1

def board(ship,prob): #argument 1: number of ships in chosen game mode, argument 2: probability of ship appearing in each row

    board = []
    row = 1
    probability = prob
    ships = ship

    while row <= 20:
        rowBoard = []
        column = 1
        while column <= 60:
            surprise = random.choice(probability)
            if ship == 0:
                rowBoard.append(0)  #continue appending "empty spots" after all ships have been spawned
                column += 1
            else:
                if surprise >= 1 and surprise <= 4 and surprise in rowBoard:
                    column = column #skip 
                else:
                    if surprise == 0:
                        rowBoard.append(surprise)
                        column += 1
                    else:
                        if surprise >= 1 and surprise <= 4:
                            for i in range(5):
                                rowBoard.append(surprise)
                        column += 5
                        ship -= 1

        board.append(rowBoard)
        row += 1

####################display########################
    displayBoard = []

    for i in range(20):
        displayBoard.append(["#"]*60)

    booms = 1
    shipCounter = 0
    while booms <= 15:
        if shipCounter == 5:
            display()
            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            print ("You've sunk my battleship!")
            attempts = booms
            booms = 16
        else:
            display()
            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            try:
                userRow, userCol = map(int, input("Enter row and col: ").split())              
                if userRow < 1 or userRow > 20 or userCol < 1 or userCol > 60:
                    print ("Sorry, this ocean isn't that big.")
                    continue
            except ValueError:
                print("Sorry, I don't understand that.")
                continue
            else:
                booms += 1
                bombed = board[userRow-1][userCol-1]
                if ships == 80: #beginner mode
                    if bombed == 5:
                        print ("You've already bombed that ship.")
                    else:
                        if bombed == 6:
                            print ("You already know there isn't a ship there.")
                        else:
                            if bombed >= 1 and bombed <= 4:
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = []
                                for n, i in enumerate(board[userRow-1]):
                                    if i == bombed:
                                        shipIndex.append(board[userRow-1].index(i))
                                        board[userRow-1][n] = 5
                                        for i in shipIndex:
                                            displayBoard[userRow-1][n] = "O"

                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "
                                
                elif ships == 50: #intermediate mode
                    if bombed == 4:
                        print ("You've already bombed that ship.")
                    else:
                        if bombed == 5:
                            print ("You already know there isn't a ship there.")
                        else:
                            if bombed >= 1 and bombed <= 3:
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = []
                                for n, i in enumerate(board[userRow-1]):
                                    if i == bombed:
                                        shipIndex.append(board[userRow-1].index(i))
                                        board[userRow-1][n] = 4
                                        for i in shipIndex:
                                            displayBoard[userRow-1][n] = "O"
                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "
                                
                elif ships == 20: #advanced mode
                    if board[userRow-1][userCol-1] == 2: 
                        print ("You've already bombed that ship.")
                    else:
                        if board[userRow-1][userCol-1] == 3:
                            print ("You already know there isn't a ship there.")
                        else:
                            if board[userRow-1][userCol-1] == 1: #if position chosen == 1 in board
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = [] #initialize index list to use for display board
                                for n, i in enumerate(board[userRow-1]): #for the row specificed by user in board list
                                        if i == 1:
                                            shipIndex.append(board[userRow-1].index(i))
                                            board[userRow-1][n] = 2
                                            for i in shipIndex:
                                                displayBoard[userRow-1][n] = "O"
                        
                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "

    if attempts >= 13 and attempts <= 15:
        print ("You are a novice.")
    elif attempts >=10 and attempts <= 12:
        print ("Not bad.")
    elif attempts < 10:
        print ("You have the talent!")
    else:
        print ("You've no luck today, try again.")

    userscore = (attempts)
    print("Your score is", userscore)

    scorefile = open('score.txt','r')
    score = scorefile.readlines()
    scorefile.close

    scorelist = []

    #put highscores into list
    for line in score:
        scorelist.append(line.split(" "))

    #change score to integer
    for item in scorelist:
        item[0]=int(item[0])
        
    #To check replace highscore or add highscore
    if len(scorelist)==10 :
        if userscore<(scorelist[-1][0]):
            print("Congratulations! You beat the highscore! :)")
            username=(input("Please enter your name: ")+"\n")
            scorelist[-1]=[userscore,username]
            list.sort(scorelist)
        else:
            print("Try harder next time. :(")
                   
    else:
        print("Congratulation! You beat the highscore! :)")
        username=(input("Please enter your name: ")+"\n")
        scorelist.append([userscore,username])
        list.sort(scorelist)
    
    writescore=open('score.txt','w')
    for item in scorelist:
        writescore.write(str(item[0])+" "+item[1])
    writescore.close()


    

print('''
´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´
''')
try:
    print("Press a to start the game \nPress b to display the highscore \nPress c to delete the highscore \nPress d to exit the game\n")
    ans=input()
    if ans =="a":
        try:
            difficulty = int(input("What difficulty would you like to play? (1=Beginner/2=Intermediate/3=Advance) "))
            if difficulty == 1:
                board(80, [0,1,0,2,0,3,0,4,0])
            elif difficulty == 2:
                board(50,[0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,3,0,0,0])
            elif difficulty == 3:
                board(20,[0,0,0,1,0,0,0,0,0,0,0,0])
        except:
            print("Please enter 1,2 or 3")
    elif ans=="b":
        displayscore()
        loop=False
    elif ans=="c":
        deletescore()
        loop=False
    elif ans=="d":
        print("Thanks you and see you next time")
        loop=False
    else:
        print("Not valid choice try again")
except ValueError:
    print("Please enter a,b,c or d")
        


def displayscore():
    readscore = open('score.txt','r')
    score = readscore.readlines()
    readscore.close

    print("HIGH SCORE")
    for line in score:
        shipCounter=(line.split("\n"))
        print(shipCounter[0])

def deletescore():
    clearscore=open('score.txt','w')
    clearscore.close


