rock = "r"
paper = "p"
scissors = "s"

player_1_score = 0
player_2_score = 0

for i in range(5):
    player_1_input = input("Enter rock paper or scissors: ")
    player_2_input = input("Enter rock paper or scissors: ")

    if player_1_input == paper and player_2_input == rock:
        print("User One Wins!")
        player_1_score += 1
    elif player_1_input == scissors and player_2_input == paper:
        print("User One Wins!")
        player_1_score += 1
    elif player_1_input == rock and player_2_input == scissors:
        print("User One Wins!")
        player_1_score += 1
    else:
        print("Player Two Wins")
        player_2_score += 1

print("\n")
print("Player one's final score is: ", player_1_score)
print("Player two's final score is: ", player_2_score)

print("\n")
if (player_1_score > player_2_score):
    print("Therefore, Player One is the winner!")
else:
    print("Therefore Player Two is the winner!")
