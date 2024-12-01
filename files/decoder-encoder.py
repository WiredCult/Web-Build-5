def getChoice():
    while True:
        try:
            myChoice = int(input("***SECRET ENCODER***\n1 - Encode\n2 - Decode\nPlease Select a task "))
            if (myChoice == 1 or myChoice == 2):
                return myChoice
        except ValueError:
            True


    # try:
    #     myChoice = int(input("Decode or Encode?: "))
    # except ValueError:
    #     print ("Bad Input")
    # else:   
    #     return myChoice

def getInput(characterList, choice):
    while True:
        myInput = input(f"Enter your input to {choice}: ")
        myInput = myInput.lower()

        for letter in myInput:
            # if (letter in characterList) == False:
            if (letter not in characterList):
                print("Incorrect character entered. Please try again.")
                break
        else:
            return myInput

def encode(userInput, characterList, encodingList):
    # loop through each letter in userInput
    # for n in range(0, len(userInput)):
    #     # print(userInput[n])

    encodedOutput = ""
    for letter in userInput:
        # find the index of the letter in characterList
        index = characterList.index(letter)
        # find the letter of the same index in encodingList
        encodedLetter = encodingList[index]
        
        # print(encodedLetter)
        encodedOutput = encodedOutput + encodedLetter
    
    print("Your encoded message is", encodedOutput)
    input("")
    
def decode(userInput, characterList, encodingList):
    # loop through each letter in userInput
    # for n in range(0, len(userInput)):
    #     # print(userInput[n])

    decodedOutput = ""
    for letter in userInput:
        # find the index of the letter in characterList
        index = encodingList.index(letter)
        # find the letter of the same index in encodingList
        decodedLetter = characterList[index]
        
        # print(decodedLetter)
        decodedOutput = decodedOutput + decodedLetter
    
    print("Your encoded message is", decodedOutput)
    input("")

def main():
    # character and encoding lists
    characterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    encodingList = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "a"]

    # get user input
    userChoice = getChoice()
    if (userChoice == 1):
        choice = "Encode"
        userInput = getInput(characterList, choice)
        encode(userInput, characterList, encodingList)
    elif (userChoice == 2):
        choice = "Decode"
        userInput = getInput(characterList, choice)
        decode(userInput, characterList, encodingList)
        
    
    
main()