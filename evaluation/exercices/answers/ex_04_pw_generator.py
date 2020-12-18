import random 

password=""
containsSymbole=False
containsNumber=False
containsMajLetter = False
containsMinLetter = False

wordIsDone=False

symbols = random.randint(33, 47)
number = random.randint(48, 58)
majLetter = random.randint(65, 91)
minLetter = random.randint(97, 123)

for i in range(0, 12):
    character= random.randint(0,3)
    if character==0 :
        containsSymbole =True
        password += chr(random.randint(33, 47))
    if character==1 :
        containsNumber = True
        password += chr(random.randint(48, 58))
    if character==2 :
        containsMajLetter = True
        password += chr(random.randint(65, 91))
    if character==3 :
        containsMinLetter = True
        password += chr(random.randint(97, 123))


while (wordIsDone==False) :
    if (containsSymbole & containsNumber & containsMajLetter & containsMinLetter) :
        wordIsDone=True
    else :
        if containsSymbole==False :
            password[-1] = chr(random.randint(33, 47))
            containsSymbole==True
        if containsNumber==False :
            password[-2] = chr(random.randint(48, 58))
            containsSymbole==True
        if containsMajLetter==False :
            password[-3] = chr(random.randint(65, 91))
            containsMajLetter==True
        if containsMinLetter==False :
            password[-3] = chr(random.randint(97, 123))
            containsMinLetter==True
        

print(password)


###Test if conditions are true

#print(len(password))
#print(containsSymbole)
#print(containsNumber)
#print(containsMajLetter)
#print(containsMinLetter)