import random
ladder={1:38,4:14,8:30,21:42,28:76,50:67,71:92,80:99}
snakes={32:10,34:6,48:26,62:18,88:24,95:56,97:78}
play1=0
play2=0
def moment(move):
    dice=random.randint(1,6)
    print(f"Score:{dice}")
    move+=dice
    if move in snake:
        print("Oh so sad Caught by a snake")
        move=snake[move]
        print(f"present in :{move}")
    elif move in ladder:
        print("Hurrah!You got a ladder")
        move=ladder[move]
        print(f"present in :{move}")
    else:
        print(f"present in :{move}")
    print("\n")
    return move
while True:
    one=input("It player1 turn to play")
    play1=moment(play1)
    if(play1>100):
        print("Player1 won the game.")
        print("Game Over")
        break
    two=input("It player2 turn to play")
    play2=moment(play2)
    if(play2>100):
        print("Player2 won the game.")
        print("Game Over")
        break
    
