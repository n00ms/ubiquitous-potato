import random

def displayscore(): 
    readscore = open('score.txt','r')
    score = readscore.readlines()
    readscore.close

    print("HIGH SCORE")
    for line in score:
        attempts = (line.split("\n"))
        print(attempts[0])

def deletescore():
    clearscore = open('score.txt','w')
    clearscore.close

#prints column numbers  
def display():
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

def board(ship,prob):   
    board = []
    #main board
    row = 1
    probability = prob
    #probability of ship appearing in a row differs depending on difficulty mode (refer to main menu)
    ships = ship 
    #total number of ships depending on difficulty mode
    
    while row <= 20:
        rowBoard = []
        column = 1
        while column <= 60:
            surprise = random.choice(probability)
            if ship == 0:
                rowBoard.append(0)
                #continue appending 'empty spots' after ship count met
                column += 1
            else:
                if surprise >= 1 and surprise <= 4 and surprise in rowBoard: 
                    column = column
                    #if duplicate (a ship represented by that number already exists), skip
                else:
                    if surprise == 0:
                        rowBoard.append(surprise)
                        column += 1
                    else:
                        if surprise >= 1 and surprise <= 4:
                            #ship represented by numbers 1 to 4
                            for i in range(5):
                                rowBoard.append(surprise)
                        column += 5
                        ship -= 1

        board.append(rowBoard)
        row += 1

    displayBoard = [] #display

    for i in range(20):
        displayBoard.append(["#"]*60)

    booms = 1
    shipCounter = 0 
    while booms <= 15: 
        if shipCounter == 5:
            #exit loop once 5 ships bombed
            display()
            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            print ("You've sunk my battleship!")
            attempts = booms - 1
            booms = 16 
        else:
            display()
            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            try:
                userRow, userCol = map(int, input("Enter location to boom (row,col): ").split())              
                if userRow < 1 or userRow > 20 or userCol < 1 or userCol > 60:
                    print ("Sorry, this ocean isn't that big.")
                    continue
            except ValueError:
                print("Sorry, I don't understand that.")
                continue
            else:
                booms += 1
                bombed = board[userRow-1][userCol-1]
                if ships == 80: #if beginner mode
                    if bombed == 5:
                        print ("You've already bombed that ship.")
                    else:
                        if bombed == 6:
                            print ("You've already know there isn't a ship there.")
                        else:
                            if bombed >= 1 and bombed <= 4: 
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = []
                                for n, i in enumerate(board[userRow-1]):
                                    #record unmasked ship in board, unmask in display
                                    if i == bombed:
                                        shipIndex.append(board[userRow-1].index(i))
                                        board[userRow-1][n] = 5
                                        for i in shipIndex:
                                            displayBoard[userRow-1][n] = "O"

                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "
                                
                elif ships == 50: #intermediate
                    if bombed == 4:
                        print ("You've already bombed that ship.")
                    else:
                        if bombed == 5:
                            print ("You've already know there isn't a ship there.")
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
                                
                elif ships == 20: #advanced
                    if board[userRow-1][userCol-1] == 2: 
                        print ("You've already bombed that ship.")
                    else:
                        if board[userRow-1][userCol-1] == 3:
                            print ("You already know there isn't a ship there.")
                        else:
                            if board[userRow-1][userCol-1] == 1: 
                                shipCounter += 1
                                print ("You've sunk my battleship!")
                                shipIndex = [] 
                                for n, i in enumerate(board[userRow-1]): 
                                        if i == 1:
                                            shipIndex.append(board[userRow-1].index(i))
                                            board[userRow-1][n] = 2
                                            for i in shipIndex:
                                                displayBoard[userRow-1][n] = "O"
                        
                            else:
                                print ("You missed!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "

    
        

    if shipCounter < 5:
        display
        countRow = 1
        for row in displayBoard:
            print("".join(row), countRow)
            countRow += 1
        print ("You've no luck today, try again.\n")

    if attempts >= 13 and attempts <= 15:
        print ("You are a novice.\n")
    elif attempts >=10 and attempts <= 12:
        print ("Not bad.\n")
    elif attempts < 10:
        print ("You have the talent!\n")

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
        item[0] = int(item[0])
        
    #To check replace highscore or add highscore
    if len(scorelist) == 10 :
        if userscore < (scorelist[-1][0]):
            print("Congratulations! You beat the highscore! :)")
            username = (input("Please enter your name: ")+"\n")
            scorelist[-1] = [userscore,username]
            list.sort(scorelist)
        else:
            print("Try harder next time. :(")
                   
    else:
        username = (input("Please enter your name: ")+"\n")
        scorelist.append([userscore,username])
        list.sort(scorelist)
    
    writescore = open('score.txt','w')
    for item in scorelist:
        writescore.write(str(item[0])+" "+item[1])
    writescore.close()


    
def mainmenu():
    loop = True
    while loop:
        print("Press a to start the game \nPress b to display the highscore \nPress c to delete the highscore \nPress d to exit the game")
        ans = input()
        if ans == "a":
            try:
                difficulty = int(input("What difficulty would you like to play? \n1 = Beginner (80 ships)\n2 = Intermediate (50 ships)\n3 = Advanced (20 ships)\n"))
                if difficulty == 1:
                    board(80, [0,1,0,2,0,3,0,4,0])
                    exit()
                elif difficulty == 2:
                    board(50,[0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,3,0,0,0])
                    exit()
                elif difficulty == 3:
                    board(20,[0,0,0,1,0,0,0,0,0,0,0,0])
                    exit()
            except:
                print("Again!")
                continue
        elif ans == "b":
            displayscore()
            mainmenu()
        elif ans == "c":
            deletescore()
            mainmenu()
        elif ans == "d":
            print("Thanks you and see you next time")
            exit()
        else:
            print("Not valid choice try again")
            mainmenu()

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
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´    Over the cerulean sea, you and your mate are setting asail, trying to escape the
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´    clutches of the British Navy ships under her Royal Majesty’s order, Queen Petunia.
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´    Ain't nothing more sinner-est than stealing from Petunia's booty locked under the 
´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´    so-called secured bank in London.Titled in bold on the front cover of News Straight
´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´    Times, your crew, the Bootleg, has once again been featured in the monthly newspaper
´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´    spread.
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
welcome = '''
                 Welcome To Battleship Mates!
                The goal is to destroy 5 ships!\n
        '''
print(welcome)

mainmenu()





