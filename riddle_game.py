#!/bin/python3
from random import randrange

#THIS IS GAME THAT GIVES A RANDOM NUMBER BETWEEN 0 AND 100 AND ALLOWS THE USER THE GUESS THIS NUMBER IN 7 ATTEMPTS. THE PLAYER WINS THE ATTEMPTS REMAINING AS POINTS IN EACH ROUND.
#YOU CAN PLAY IT WITH FRIENDS AND SEE WHO IS THE BEST IN A RIDDLE. EACH PLAYER HAS 5 ROUNDS TO PLAY AND TO GET THE HIGHER SCORES HE COULD HAVE WON.


#A FUNCTION TO TAKE INFORMATIONS ABOUT THE PLAYERS

def players():
    number = int(input("Enter the players number: ")) #reading the players number
    list_of_players = [] #Create a list for saving their informations
    x = 1 #a random variable in order to control the while loop
    while x<=number:
        print("Enter the name of the player no.",x,":", end="") #Player number 1, 2, 3, ....
        names = input() #Reading names
        list_of_players.append(names) #Saving names in the list
        x = x+1 #Iteration
    return list_of_players #Take the whole names in the list, so we can use it in another function or in the main one





#A FUNCTION STARTING AND SUCCESSIVELY PLAYING THE GAME IN EACH PLAYER'S TURN, TAKING AND SAVING THEIR POINTS BY A RETURN FUNCTION

def turn(player):
    print("\n\n-->",player,"<-- It's your turn !!!")
    points = 0 #Initiate the points, so we can add it after each round
    round = 1 #Initiate the round
    while round<=5:
        number_to_guess = randrange(0,100) #Taking the MAGIC NUMBER
        print('\n\nROUND',round,':')
        attempt = 7
        while attempt>0: #ATTEMPT LOOP
            print("Attempt(s):",attempt) #Display the attempts remaining in each round after
            my_number = int(input('Try to guess the random number: ')) #Reading the number I entered and take as an integer variable
            if my_number<number_to_guess:
                print('-->',my_number,'<-- is less than the right one!!!\n') #Display a little hint in the game
            elif my_number>number_to_guess:
                print('-->',my_number,'<-- is greater than the right one!!!\n') #Display a little hint in the game
            else:
                print("Good job!!! -->",my_number,"<-- is exactly the number to guess\nYou won",attempt,"point(s)\n") #Say to the player he was right
                points = points + attempt #Take all attempts remaining as point
                break #Stop the #ATTEMPT LOOP, so we can start a new round
            attempt = attempt-1 #Subtract the attempts remaining after a bad response
            if attempt ==0:
                print("The number to guess was",number_to_guess,"!!!!") #Display the MAGIC NUMBER if the player have not found the right response after 7 attempts
        round = round+1 #Going to the next round
    print("\n\n-->",player,"<-- GOT",points,"POINTS IN THIS ROUND") #Display the total points earned by the player during his turn
    return points #It allows us to save and/or to add each player's scores in a table or in a variable when we use the function




#A FUNCTION COMPARING EACH PLAYER'S SCORES AND DESCRIBE THE WINNER BETWEEN THEM

def winner(table_of_scores, players):
    x = 0 #a random variable in order to control the while loop
    maximum = 0 #Initiating
    while x<len(players): #A while loop to compare each range of the table
        if maximum<=table_of_scores[x]:
            maximum = table_of_scores[x]
            winner = players[x]
        else:
            maximum = maximum
            winner = winner #Saving the name of the player having the higher score
        x = x+1
    return winner
    

players = players() #Calling the PLAYERS() function
scores = [] #Creating the table of scores
a = 0 #a random variable in order to control the while loop
while a<len(players):
    score.append(turn(players[a])) #Calling the TURN() function and putting scores in the table
    a = a+1 #Iteration



#DISPLAY THE SCORES AND TELL WHO IS THE WINNER

print("\n\n\n\tSCORES TABLE")
b = 0 #a random varible in order to control the while loop
while b<len(scores):
    print(players[b],"------>",scores[b],"points\n")
    b = b+1
print("\n\tWINNER ------->",vainqueur(scores, players),"\n\tCONGRATULATIONS !!!!!")
