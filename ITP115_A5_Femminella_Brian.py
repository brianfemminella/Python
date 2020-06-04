# Brian Femminella
# ITP 115, Fall 2019
# Assignment #5

import random

#Part 1- Word Jumble Game

def main():
    wordList = ["goldfish", "potato", "President", "kanye", "skiier"]
    hintList = ["the snack that smiles back", "hearty vegetable", "oval office ", "best rap artist", "Big Bear Mountain"]
    answer = random.choice(wordList)
    answerIndex = wordList.index(answer)  # Used for the hint later
    jumbledWordList = ["Blank"] * len(
        answer)  # Make a list with the word "blank" the same number of times as letters in answer
    i = 0

    # Jumble word and save to jumbledWordList
    while "Blank" in jumbledWordList:
        randIndex = random.randrange(0, len(answer))
        if jumbledWordList[randIndex] == "Blank":  # provided the random index generated has not been filled already...
            jumbledWordList[randIndex] = answer[i]
            i += 1

    # Convert jumbledWordList into string jumbledWord
    jumbledWord = ''.join(jumbledWordList)
    print("The jumbled word is '" + jumbledWord + "'")

    # Start game
    guess = " "
    numTries = 1
    while guess != answer: #until your guess is equal to your answer
        guess = input("Please enter your guess: ")
        if guess == answer:
            print("You got it!")
            print("It took you " + str(numTries) + " tries.")
        else:
            print("Try again.")
            numTries += 1
            if (numTries == 6):
                print("Hint: " + hintList[answerIndex])

main()


#Part 2- Encrypt/Decrypt

def main():
    # Generate alphabetlist
    alphabetList = [" "] * 26
    for i in range(97, 123):
        alphabetList[i - 97] = chr(i)

    # Prompt user for inputs
    message = input("Enter a message: ")
    shift = int(input("Enter a number to shift by (0-25): "))

    # Make list with shifted values
    shiftedList = [" "] * 26
    counter = 0
    for z in range(0, 26):
        if (z + shift <= 25):
            shiftedList[z] = alphabetList[z + shift]
        else:
            shiftedList[z] = alphabetList[counter]
            counter += 1

    # Make encrypted message
    encryptedMessageList = [" "] * len(message)
    counter = 0
    for char in message:
        if char in shiftedList:
            index = alphabetList.index(char)
            encryptedMessageList[counter] = shiftedList[index]
        counter += 1

    # Make encrypted message into string
    encryptedMessage = ''.join(encryptedMessageList)

    # Decrypt Message
    decryptedMessageList = [" "] * len(encryptedMessage)
    counter = 0
    otherCounter = 25
    for char in encryptedMessage:
        if char in alphabetList:
            index = shiftedList.index(char)
            if (index - shift < 0):
                otherCounter -= index + shift
                decryptedMessageList[counter] = alphabetList[otherCounter]
                otherCounter += 1
            else:
                decryptedMessageList[counter] = alphabetList[index - shift]
        counter += 1

    print("Encrypting message....")   #print statements to show the results of the code are as follows:
    print("\t Encrypted Message: " + encryptedMessage)
    print("Decrypting message....")
    print("\t Decrypted Messge: " + message)
    print("\t Original Message: " + message)


main()
