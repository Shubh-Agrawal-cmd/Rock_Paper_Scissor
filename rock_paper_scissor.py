"""This is a simple implementation of a popular game Rock-Paper-Scissor
                   By Shubh Agrawal"""
import random
def game(computer_points,user_points):
    rock_paper_scissor = ["Rock", "Paper", "Scissor"] # List to choose from
    value_of_rock_paper_scissor = {"Rock" : 82, "Paper" : 112, "Scissor" : 115} # ASCII values of r,p,s given to each for comparision later
    n = random.randint(0,2) # Random number between 0-2,since length of list is 3   
    def retry():
        print('''Press....
            "r" for Rock.
            "p" for Paper.
            "s" for Scissor.''')
        global user_input  # declared Global as used outside function's scope
        user_input = input()
        user_input = user_input.lower()
        if user_input == "r":
            user_input = "Rock"
        elif user_input == "p":
            user_input = "Paper" 
        elif user_input == "s":
            user_input = "Scissor"
        else:
            print("Retry!!!")
            retry() # Recursively called until user passes correct input
    retry()        
    computer_input = rock_paper_scissor[n] # A random choice from the list
    print("You Chose " + str(user_input) + " and Computer Chose " + str(computer_input)) # made on Py 3.4.3 so doesn't supports f srting 
    value_of_rock_paper_scissor["Scissor"] = 81 if ((user_input or computer_input) == "Rock") else 115  # Since r > p > s in ASCII
                                                                                                        # only when one choice is Rock we change the value of Scissor
                                                                                                        # so that it is less than rock

    if value_of_rock_paper_scissor[user_input] != value_of_rock_paper_scissor[computer_input]:
        if value_of_rock_paper_scissor[user_input] < value_of_rock_paper_scissor[computer_input]:   # Condition for Loosing
            print("Sorry, Computer Wins!!!")
            computer_points += 1
            print("Points :\n Computer: " + str(computer_points) + "\n User: " + str(user_points))
        elif value_of_rock_paper_scissor[user_input] > value_of_rock_paper_scissor[computer_input]:  # Condition for Winning
            print("Congratulations, You Won!!!")
            user_points += 1
            print("Points :\n Computer: " + str(computer_points) + "\n User: " + str(user_points))
    else:
        print("It is a Draw!!!")
        print("Points :\n Computer: " + str(computer_points) + "\n User: " + str(user_points))  # Condition for Draw
    print("Do you want to Challenge the Computer again? ")  # Replay the game
    print("""Press:
        Any Key --> Yes
        Return --> NO""")
    key = input()
    key = bool(key)
    if key:
        game(computer_points,user_points)  # Called the function with current points recursively
    else:
        print("Thank you for playing, Final points are : ")
        print("Points :\n Computer: " + str(computer_points) + "\n User: " + str(user_points))  # exit from game and final points
        if (computer_points > user_points):
            print("Sorry, You lost in the end ")
        elif (computer_points < user_points):
            print("Congratulations, You managed to beat the Computer ")
        else :
            print("You both Drew ")
        
game(0,0)  # Calling the function for the first time

