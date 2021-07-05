#Rock, Paper, Scissors Project (First to 3 wins).

#Import random module.
import random 

#Variables to hold for userNum and compNum
userNum = 0
compNum = 0
userInput = ''

#Welcome the user.
print("Welcome to rock, paper, scissors!")

#Prompt the user to enter S or E to start or end the game.
userInput = input("Please enter 'S/s' to start or 'E/e' to exit.")
print()

#Initialize playAgain if user wants to play again.
playAgain = "y"

while ((playAgain == "y") or (playAgain == "Y")):

    #Loop to enter a valid input (alphabet).
    while ((userInput != 'S') and (userInput != 's') and (userInput != 'E') and (userInput != 'e')):

        #Error message and input.
        userInput = input("Please enter a valid input ('S/s' to start or 'E/e' to exit).")
    
    #Determine if user wants to start or exit.
    if ((userInput == 'S') or (userInput == 's')):

        #Initialize userScore, compScore, and playAgain.
        userScore = 0
        compScore = 0

        #While loop to begin game until user or comp gets 3 wins.
        while (((userScore < 3) and (compScore != 3)) or ((compScore < 3) \
                and (userScore != 3))):

            #Prompt user to enter a number from 1 to 3.
            userNum = input("Enter a number from one to three. (1:Rock, 2:Paper, 3:Scissors)")
            print()

            #Loop if user enters invalid input.
            while ((userNum != "1") and (userNum != "2") and (userNum != "3")):

                #Prompt user to enter a valid input.
                userNum = input("Please enter a number from one to three.")
                print()

            #Determine what user chose and print it.
            if userNum == "1":

                #Print rock.
                print("You chose rock.")

            elif userNum == "2":

                #Print paper.
                print("You chose paper.")

            elif userNum == "3":

                #Print scissors.
                print("You chose scissors.")

            #Convert userNum to int.
            userNum = int(userNum)
        
            #Generate a random number from 1 to 3 for compNum.
            compNum = random.randint(1, 3)

            #Determine what computer chose and print it.
            if compNum == 1:

                #Print rock.
                print("The computer chooses rock.")

            elif compNum == 2:

                #Print paper.
                print("The computer chooses paper.")

            elif compNum == 3:

                #Print scissors.
                print("The computer chooses scissors.")
            
            #Determine winner of the match.
            #If userNum wins.
            if (((userNum == 1) and (compNum == 3)) or ((userNum == 2) and (compNum == 1)) \
                or ((userNum == 3) and (compNum == 2))):

                #Add a point to userScore.
                userScore += 1

                #Print score.
                print("You get a point.")
                print("User:", userScore, "Computer:", compScore)

            #If compNum wins.
            elif (((compNum == 1) and (userNum == 3)) or ((compNum == 2) and (userNum == 1)) \
                or ((compNum == 3) and (userNum == 2))):

                #Add a point to compScore.
                compScore += 1

                #Print score.
                print("Computer gets a point.")
                print("User:", userScore, "Computer:", compScore)

            #If tied.
            elif (userNum == compNum):

                #Print score.
                print("Tied, User:", userScore, "Computer:", compScore)

                #Continue.
                continue

            print()

            #Determine and print the winner of the game.
            #If user wins.
            if userScore == 3:

                #Print congradulations.
                print("Congradulations you win over the computer", userScore, "to", compScore, end="!/n")

            #If computer wins.
            elif compScore == 3:

                #Print computer wins.
                print("The computer wins", compScore, "to", userScore, end="!\n")

    #If user wants to exit.
    elif ((userInput == "E") or (userInput == "e")):

        #Print exit.
        print("Exiting the game. Goodbye!")

    #Prompt the user if they would like to play again.
    playAgain = input("Would you like to play again? (Enter y or Y to continue, or enter any other character to leave.)")
    print()
    
#Thank user and goodbye.
print("Thank you for playing! Goodbye!")



    

    

        
            
        
                                                       
                                            

        

    

