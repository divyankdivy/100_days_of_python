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

import random
print("Welcome to Rock Paper Scissors")

user_choice = int(input("Enter your choice, 1 for rock, 2 for paper and 3 for scissors: "))
print('user choice is',end = ': ')
if user_choice == 1:
    print('rock\n',rock)
elif user_choice == 2:
    print('paper\n',paper)
elif user_choice == 3:
    print('scissors\n',scissors)

machine_choice = random.randint(1,3)
print('machine choice is', end = ': ')
if machine_choice == 1:
    print('rock\n',rock)
elif machine_choice == 2:
    print('paper\n',paper)
elif machine_choice == 3:
    print('scissors\n',scissors)

if user_choice == machine_choice:
    print("It's a Tie")
elif user_choice == 1 and machine_choice == 2:
    print('You Loose')
elif user_choice == 1 and machine_choice == 3:
    print('You Win')
elif user_choice == 2 and machine_choice == 1:
    print("You Win")
elif user_choice == 2 and machine_choice == 3:
    print("You Loose")
elif user_choice == 3 and machine_choice == 1:
    print('You Loose')
elif user_choice == 3 and machine_choice == 2:
    print('You Win')