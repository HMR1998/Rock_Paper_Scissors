import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

player_choice = int(input("what  do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_image[player_choice])



comp_choice = random.randint(0, 2)
print(f"Computer has chosen: ")
print(game_image[comp_choice])


if (player_choice >= 3) or player_choice < 0:
    print("INVALID INPUT, you lose!")
elif (player_choice == 0) and (comp_choice == 2):
    print("You Win!")
elif (comp_choice == 0) and (player_choice == 2):
    print("You lose!")
elif comp_choice > player_choice:
    print("You Lose!")
elif player_choice > comp_choice:
    print("You win!")
elif comp_choice == player_choice:
    print("Its a draw!")
