
n =""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_input = input("Quel est le nombre maximum? \n")
#print(type(int(user_input)))

try:
    n=int(user_input)
except ValueError:
   pass


while (type(n)!= int):
        user_input = input("Quel est le nombre maximum? \n")
        try:
            n=int(user_input)
        except ValueError:
            pass


if (type(n)== int) :
    for number in a:
        if (number < n):
            print(number)



