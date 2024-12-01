import random

def getNameInput():
    # start the loop
    while True:
        # get user input
        getName = input("Enter victims name: ")
        # if name is a space or starts with a space return an error
        if getName == (' '):
            print ("Invalid Input - Name cannot be empty")
        elif getName.startswith(' '):
            print ("Invalid Input - Name cannot start with a space")
        # if input is valid return the variable and end the loop
        else:
            return getName

def getInsultInput():
    # start the loop
    while True:
        # get user input
        try:
            insultNum = int(input("How many insults do you want to generate?: "))
            # if the input is greater than zero return the value and end the loop
            if insultNum > 0:
                return insultNum
            # if the input is less than zero return an error
            else:
                print ("Invalid Input - Please enter a whole number")
        # if the input is not a number return an error
        except ValueError:
            print ("Invalid Input - Please enter a whole number")
        
def getAdjectiveInput():
    # Start the loop
    while True:
        # get user input
        try:
            adjectiveNum = int(input("How many adjectives per insult? (Max 3): "))
            # if the input is less than or equal to 0 return an error
            if adjectiveNum <= 0:
                print ("Invalid Input - Please enter a whole number")
            # if the input is greater than 3 return an error
            elif adjectiveNum > 3:
                print ("Invalid Input - Max adjectives is 3")
            # return the input if it is valid
            else:
                return adjectiveNum
        # if the input is not a number return an error
        except ValueError:
            print ("Invalid Input - Please enter a whole number")


def main():
    # start the main loop
    while True:
        # get the data from the functions
        victimName = getNameInput()
        insultAmount = getInsultInput()
        adjectiveAmount = getAdjectiveInput()

        # create the adjective and noun lists
        adjectives = ["Smelly","Stinky","Goofy","Little","Big","Ghastly","Tiny","Yucky","Horrible","Fanatical"]
        nouns = ["Ghoul","Nematode","Sponge","Goober","Monster","Zombie"]

    
        # build the insult the amount of times requested
        for n in range(insultAmount):
            # start the insult string with the victims name
            insult = (f"{victimName} is a ")
            # join adjectives to the insult string based on amount requested
            insult = insult + ' '.join(random.sample(adjectives, adjectiveAmount))
            # add the noun to the end of the string with an exclaimation point
            insult = insult + ' ' + random.choice(nouns) + '!'
            # print the insult
            print(f"\033[34m{insult}\033[0m")

        # start another loop for the ending prompt
        while True:
            # ask the player if they want to play again. Convert input to uppercase.
            playAgain = input("Do you want to play again?(Y)(N) ").upper()
            # if the input is y break the loop to play again
            if playAgain == "Y":
                break
            # if the input is n quit the program
            elif playAgain == "N":
                quit()
            # if the input is not y or n return an error
            else:
                print ("Invalid Input - Y to play again or N to quit")


main()