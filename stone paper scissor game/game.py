import random

def game(player,computer,c):
    
    if((player=='stone' and computer=='stone') or(player=='paper' and computer=='paper') or (player=='scissor' and computer=='scissor')):
            print("draw")
    elif(player=='stone'and computer=='scissor') or (player=='paper'and computer=='stone') or (player=='scissor'and computer=='stone'):
            
            if(c==1):
                print("player-1 won")
            else:
                print("player won")
    else:
            if(c==2):
                print("computer won")
            else:
                print("player-2 won")
bool=True
while bool:
    print('''
         1.Two player

         2.One player
    ''')
    l=['stone','paper','scissor']

    c=int(input("enter your choice : "))
    if c==2:
        bool=False
        print('''
             1.stone
             
             2.paper
             
             3.scissor

        ''')
        contin='Y'
        while(contin=='Y' or contin=='y'):
            player_index=int(input("enter your choice : "))
            player=l[player_index-1]
            computer=l[random.randint(0,2)]
            print("\n")
            print("Your choice ->",player)
            print("\n")
            print("computer choice ->",computer)
            print("\n")
            print(player,' vs ',computer)
            print("\n")
            game(player,computer,c)
            print("\n")
            contin=input("Do you want to continue say 'Y' or 'N' : ")
            if(contin=='N'):
                break

    elif c==1:
        bool=False
        print('''
             1.stone
             
             2.paper
             
             3.scissor

        ''')
        contin='Y'
        while(contin=='Y' or contin=='y'):
            print("\n")
            player1_index=int(input("enter player 1 choice : "))
            print("\n")
            player2_index=int(input("enter player 2 choice : "))
            player1=l[player1_index-1]
            player2=l[player2_index-1]
            print("\n")
            print("Player-1 choice ->",player1)
            print("\n")
            print("Player-2 choice ->",player2)
            print("\n")
            print(player1,' vs ',player2)
            print("\n")
            game(player1,player2,c)
            print("\n")
            contin=input("Do you want to continue say 'Y' or 'N' : ")
            if(contin=='N'):
                break
        

        

    else:
        print("Enter correct value")
        
