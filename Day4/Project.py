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
---" ____)____
          _____)
          _______)
         _______)
---. ____________)

'''

scissors = '''
    _______
---" ____)____
          _____)
       ____________)
      (____)
---. __(____)

'''

rpc = [rock, paper, scissors]

rock_paper_scissors = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(rpc[rock_paper_scissors])

computer = random.randint(0,2)
if rock_paper_scissors >= 3 or rock_paper_scissors < 0:
    print("You typed an invalid number. You lose!")
elif computer == 2 and rock_paper_scissors == 0:
    print(f"Computer chose: \n{rpc[computer]}")
    print("You win!")
elif computer == 0 and rock_paper_scissors == 2:
    print(f"Computer chose: \n{rpc[computer]}")
    print("You lose!")
elif computer > rock_paper_scissors:
    print(f"Computer chose: \n{rpc[computer]}")
    print("You lose!")
elif computer < rock_paper_scissors:
    print(f"Computer chose: \n{rpc[computer]}")
    print("You win!")
elif computer == rock_paper_scissors:
    print(f"Computer chose: \n{rpc[computer]}")
    print("It's a draw")
