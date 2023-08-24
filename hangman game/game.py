import random
totallist=['apple','orange','banana','papaya','lemon','gooseberry','lion','tiger','elephant','bear','giraffe','camel']

flist=['apple','orange','banana','papaya','lemon','gooseberry']
alist=['lion','tiger','elephant','bear','giraffe','camel']
ran=random.randint(0,len(totallist))
ans=totallist[ran]
ans1=ans
name=(input("enter your name : "))
print("hello "+name)
l=[]
for i in range(len(ans)):
    l.append('_')
    
guess=print("your guessing letters")
for j in l:
    print(j,end=" ")
c=0
while True:
    if(c==15):
        print("\nBetter luck next time")
        break
    if(c==10):
        if ans1 in flist:
            print("/nHint : it is a fruit name")
        else:
            print("/nHint : it is a animal name")
        
    guess=input("\nenter the letter : ").lower().strip()
    
    if guess in ans:
        index=ans.find(guess)
        l.pop(index)
        l.insert(index,guess)
        for j in l:
            print(j,end=' ')
        if '_' not in l:
            print("\nYou Won the game")
            break
    else:
        for j in l:
            print(j,end=' ')
    c=c+1
print('Answer is ',ans1)

    
