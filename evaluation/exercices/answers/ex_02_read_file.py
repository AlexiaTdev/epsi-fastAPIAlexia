
myFile = open('evaluation/exercices/answers/nameslist.txt', 'r+')
text = myFile.read()
textList = text.split()

listeNoms = []
nomPresent = False

for element in textList :
    nomPresent = False
    for nom in listeNoms:
        if element == nom[0] :
            nom[1] = int(nom[1]) + 1
            nomPresent = True
    if  nomPresent==False :
        listeNoms.append([element, 1])
                
        
for nom in listeNoms :
    print(nom[0] + " : "+ str(nom[1]))
