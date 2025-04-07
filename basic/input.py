import sys
import random

title = "Enter...\n 1 for Rock,\n 2 for Paper,\n 3 for Scissors\n\n"
print(title)

user_input = input("Enter your choice: ")
player = int(user_input);
if player < 1 or player > 3:
    sys.exit("Invalid input. You must select 1, 2, or 3.")

computer_choice = random.choice("123")
computer = int(computer_choice)

print("You chose: ", user_input)
print("Computer chose: ", computer_choice)

if player == computer:
    print("It's a tie!")
elif player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
else:
    print("You lose!")