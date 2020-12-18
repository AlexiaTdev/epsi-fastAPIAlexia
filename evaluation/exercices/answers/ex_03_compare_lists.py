myFile = open('evaluation/exercices/answers/primenumbers.txt', 'r+')
text = myFile.read()
intList = text.split()

myFile2 = open('evaluation/exercices/answers/happynumbers.txt', 'r+')
text2 = myFile2.read()
intList2 = text2.split()

listDisplayed = []

for number1 in intList :
    for number2 in intList2 :
        if (number1 in intList2) & (number1 not in listDisplayed) :
            listDisplayed.append(number1)
        if (number2 in intList) & (number2 not in listDisplayed) :
            listDisplayed.append(number2)

for element in listDisplayed:
    print(element)