import random

#Recuperation des mots de words.txt sous forme de liste
myFile = open('evaluation/project/words.txt', 'r+')
text = myFile.read()
textList = text.split()

#données d'initialisation
wordIsFound=False
guessesNumber = 6
indexMysteryWord = random.randint(0, len(textList)+1)

#trois versions du mot mystere :
#   mysteryWord est le mot complet
#   discoveredWord est le tableau contenant chaque caractère découvert, au bon indice
#   displayedWord est le mot affiché, après être transofrmé par modifyDisplayedWord
mysteryWord = textList[indexMysteryWord]
discoveredWord = ["_"]
displayedWord = ""


#Initialise le tableau discoveredWord et renvoie displayedWord
def initialize():
    print(">>> Welcome to Hangman!")
    for i in range(0, len(mysteryWord)-1):
        discoveredWord.append("_")
    displayedWordInit = modifyDisplayedWord()
    print(displayedWordInit)

#réécris le mot affiché displayedWord à partir de la liste discoveredWord
def modifyDisplayedWord():
    displayedWord=""
    for element in discoveredWord :
        displayedWord = displayedWord + element + " "
    print(displayedWord)

#verifie si le jeu est gagné    
def verifyWin():
    wordIsFound=False
    jeuNonFini = False
    for element in discoveredWord:
        if element == "_":
            jeuNonFini = True
    if jeuNonFini==False:
        print("Well done !")
        wordIsFound=True
    return wordIsFound


#main
displayedWord=initialize()

while (wordIsFound==False) :
    user_input = input(">>> Guess your letter:")
    if (user_input in mysteryWord) & (len(user_input)==1) :
        index=0
        for i in mysteryWord:
            if i==user_input :
                discoveredWord[index] = user_input
            index+=1
        
        modifyDisplayedWord()
        wordIsFound=verifyWin()
    else :
        if(guessesNumber>0) :
            print(f"Incorrect! You have {guessesNumber} more guesses...")
            guessesNumber-=1
            modifyDisplayedWord()
        else :
            print(f"Incorrect again, you have lost the Hangman game! The word was {mysteryWord}")
            wordIsFound =True


    

