
print("The rules of rock,paper and scissors game are as follows:"
+"--- rock vs scissors >> rock wins"
+"--- paper vs scissors >> scissors wins"
+"--- rock vs paper >> paper wins")


computer_points=0
player_points=0
player="notend"

while player!="end":
    from random import randint
    x=["rock","paper","scissors"]
    computer=(x[randint(0,2)])
    player=str(input("enter rock/paper/scissors : "))
    print("player's choice",player)
    print("computer's choice",computer)
    if player!="end":
        print(player,"vs",computer)

    if(computer=="rock" and player=="scissors"):
        print("you loose and computer wins!")
        computer_points+=1
        print("computer: ",computer_points)
        print("player: ",player_points)
    elif(computer=="paper" and player=="rock"):
        print("you loose and computer wins!")
        computer_points+=1
        print("computer: ",computer_points)
        print("player: ",player_points)
    elif(computer=="scissors" and player=="paper"):
        print("you loose and computer wins!")
        computer_points+=1
        print("computer: ",computer_points)
        print("player: ",player_points)
    elif(computer=="scissors" and player=="rock"):
        print("you won and computer lost")
        player_points+=1
        print("player: ",player_points)
        print("computer: ",computer_points)
    elif(computer=="rock" and player=="paper"):
        print("you won and computer lost")
        player_points+=1
        print("player: ",player_points)
        print("computer: ",computer_points)
    elif(computer=="paper" and player=="scissors"):
        print("you won and computer lost",)
        player_points+=1
        print("player",player_points)
        print("computer: ",computer_points)
    elif(computer==player):
        print("its a tie")
        player_points+=1
        computer_points+=1
        print("computer: ",computer_points)
        print("player: ",player_points)
    elif player=="end":
        print("final_computer_points:",computer_points)
        print("final player_points: ",player_points)
        if(player_points>computer_points):
            print("player wins!!")
        elif(player_points<computer_points):
            print("computer wins!!")
        elif(computer_points==player_points):
            print("its a tie")
        print("bye see you next time")
        
    else:
        print("is not valid input")
