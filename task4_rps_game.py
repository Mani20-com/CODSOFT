import random
print("0=rock, 1=paper, 2=scissors")
user_choice=int(input("Enter your choice: type 0 for Rock, 1 for Paper, 2 for scissors"))
computer_choice=random.randint(0,2)
choices=["rock", "papers", "scissors"]
print(f"\nyou chose: {choices[user_choice]}")
print(f"computer chose: {choices[computer_choice]}")
if user_choice==computer_choice:
    print("it's a draw")
elif (user_choice==0 and computer_choice==2) or \
     (user_choice==1 and computer_choice==0) or \
     (user_choice==2 and computer_choice==1):
    print("you win")
else:
    print("you lose")    

            