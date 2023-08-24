#number guessing game
import random
name=input("Enter your name : ")
print("Hello "+name)
print("welcome to Number Guessing Game")
lower=int(input("Enter the range first number : "))

upper=int(input("Enter the range last number : "))
bool=True
while bool:
    if(upper<=lower):
        print("please enter the number greater than ",lower,end=" ")
        upper=int(input())
    else:
         bool=False
ans=random.randint(lower,upper)
print(ans)
bool=True
count=0      
def clue():
    if(count==5):
        r1=ans-5
        r2=ans+5
        if(r1<lower):
            r1=lower
        if(r1>upper):
            r2=upper
        print("The number is between ",r1,"and",r2)
        print("This is your last chance")

def gameover():
    global bool
    if(count==6):
        print("Game over")
        bool=False
while bool:
    guess=int(input("Enter the guess number : "))
    if(guess == ans):
        count=count+1
        gameover()
        print("Congratulation! you got the answer")
        print("No of guess is ",count)
        clue()
        
        break
    elif(guess < ans):
        count=count+1
        gameover()
        print("Try again! Your answer is too small")
        clue()
        
    else:
        count=count+1
        gameover()
        print("Try again! Your answer is too high ")
        clue()
        

