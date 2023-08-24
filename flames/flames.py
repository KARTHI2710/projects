
name1=list(input("Enter the first name : "))
name2=list(input("Enter the second name : "))
lenname1=len(name1)
lenname2=len(name2)
if(lenname1 > lenname2):
    t=name1
    name1=name2
    name2=t
print(name1)
print(name2)
for i in range(4):
    if name1[i] in name2:
        index1=name1.index(name1[i])
        index2=name2.index(name1[i])
        name1.pop(index1)
        name2.pop(index2)
        print(name1)
        print(name2)
        i=-1

    
