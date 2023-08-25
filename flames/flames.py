def flamesfunc(l):
    if l[0] == 'f':
        print("Friends")
    elif l[0] == 'l':
        print("Love")
    elif l[0] == 'a':
        print("Affection")
    elif l[0] == 'm':
        print("Marriage")
    elif l[0] == 'e':
        print("Enenmy")
    else:
        print("Sister")

bool=True
while bool:
    
    name1=list(input("Enter the first name : ").replace(" ",''))
    name2=list(input("Enter the second name : ").replace(" ",''))
    '''
    lenname1=len(name1)
    lenname2=len(name2)
    if(lenname1 > lenname2):
        t=name1
        name1=name2
        name2=t
'''
    '''
    print(name1)
    print(name2)'''
    i=0

    while(i<len(name1)):
        if name1[i] in name2:
            index1=name1.index(name1[i])
            index2=name2.index(name1[i])
            name1.pop(index1)
            name2.pop(index2)
           
            i=i-1
        i=i+1

    str=name1+name2
    length=len(str)
    flames=['f','l','a','m','e','s']
    #print(length)
    #print(str)
    j=-1
    while True:
        #print("Length of the flames list is ",len(flames))
        for i in range(0,length):
             j=j+1
             if j==len(flames):
                 j=0
             #print("i = ",i)
             #print("j = ",j)
        flames.pop(j)
        j=j-1
        print(flames)
        
        if(len(flames)==1):
            break
    flamesfunc(flames)
    bool=int(input("enter 0 to 'exit'  (or) enter 1 to 'continue' : "))

