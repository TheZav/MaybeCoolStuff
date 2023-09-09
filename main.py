import random
p = input("rock, paper, scissors  ")
r = random.randint(1,3)
if p == "rock":
  if r == 1:
    print("You choose",p)
    print("I choose rock")
    print("Let's try again")
  if r == 2:
    print("You choose",p)
    print("I choose paper")
    print("I win")
  if r == 3:
    print("You choose",p)
    print("I choose scissors")
    print("You win")
elif p == "paper":
  if r == 1:
    print("You choose",p)
    print("I choose rock")
    print("You win")
  if r == 2:
    print("You choose",p)
    print("I choose paper")
    print("Let's try again")
  if r == 3:
    print("You choose",p)
    print("I choose scissors")
    print("I win")
elif p == "scissors":
  if r == 1:
    print("You choose",p)
    print("I choose rock")
    print("I win")
  if r == 2:
    print("You choose",p)
    print("I choose paper")
    print("You win")
  if r == 3:
    print("You choose",p)
    print("I choose scissors")
    print("Let's try again")