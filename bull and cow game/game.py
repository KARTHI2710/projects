import random
code=list(map(int,input("enter a code  : ")))

def getinput1():
    while True:
        guess=list(map(int,input("guess a 4 digit number with different digits : ")))
        if(len(set(guess)) != len(guess)):

            #guess=list(map(int,input("guess a 4 digit number with different digits : ")))
            print("all the digits must be separate")
        else:
            return guess
        
chance=0
while True:
    guess=getinput1()
    chance=chance+1

    #lcode=list(map(int,str(code)))
    #print(code)
    j=0
    cow=0
    bull=0
    for i in guess:
        if i in code:
            cow=cow+1
        if guess[j]==code[j]:
            bull=bull+1
        j=j+1
    print("response : ",bull," bulls",cow-bull,' cow')
    if(guess==code):
        print("You got the answer")
        break
    if(chance==10):
        print("you loss the game")
        break


