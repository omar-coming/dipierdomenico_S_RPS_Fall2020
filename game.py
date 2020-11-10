from random import randint

choices = ["Rock", "Paper", "Scissors"]
score = 0

playername = input("Your name is?")
player = input("Choose Rock Paper or Scissors")

## ai choice
computer = choices[randint(0,2)]

if (computer == player):
    print("Computer also chose ", player)
    print("TIE")
elif(computer == "rock"):
    if(player == "scissors"):
        print("Computer Chose: ", computer, "and ", playername, " Chose: ", player)
        print("YOU LOSE!")
        score-1
    else:
        print("Computer Chose: ", computer, "and ", playername, " Chose: ", player)
        print("YOU WIN!")
        scpre+1




print(score)



