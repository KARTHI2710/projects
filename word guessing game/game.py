import random

name=input("Enter your name : ")
print("Welcom "+name)
totallist=['apple','ball','cat','dog','elephant','egg']
length=len(totallist)
ran=random.randint(0,length-1)
#print("ran",ran)
ans=totallist[ran]
#print("ans",ans)
length=len(ans)
#print("length ",length)
l=[]
for i in range(0,length):
    l.append('_')

print("You have only 15 chances")
print("Good Luck")
i=0
print("guess the letters")
for j in l:
    print(j)

c=0   
while(i<length):
    
        if(c==15):
            print("Better Luck Next Time")
            break
        str=(input("guess the letter : ")).lower().strip()
        
        if str in ans[i] and str != '':
            l.insert(i,str)
            l.pop()
            i=i+1
            for j in l:
               print(j)
            if(l[length-1]!='_'):
                print("You Won the game")
                break
        else:
            for j in l:
               print(j)
        c=c+1   
    
