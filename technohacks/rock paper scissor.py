def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if (player1[p1]==player2[p2]):
        print("draw")
    elif(player1[p1]=="rock" and player2[p2]=="scissor"):
        print("player1 wins")
    elif(player1[p1]=="rock" and player2[p2]=="paper"):
        print("player2 wins")
    elif(player1[p1]=="paper" and player2[p2]=="scissor"):
        print("player2 wins")
    elif(player1[p1]=="paper" and player2[p2]=="rock"):
        print("player1 wins")
    elif(player1[p1]=="scissor" and player2[p2]=="rock"):
        print("player2 wins")
    elif(player1[p1]=="scissor" and player2[p2]=="paper"):
        print("player1 wins")
player1={0:"rock",1:"paper",2:"scissor"}
player2={0:"paper",1:"rock",2:"scissor"}
while(1):
    num1=input("player 1,enter your choice: ")
    num2=input("player 2,enter your choice: ")
    bit1=int(input("player 1,enter the secret bit position: "))
    bit2=int(input("player 2,enter the secret bit position: "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("do you want to continue? y/n: ")
    if(ch=="n"):
        break
