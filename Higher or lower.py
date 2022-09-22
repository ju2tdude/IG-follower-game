import random
from Game_data import data
from art import logo
from art import vs

z = True
score = 0
hold = 0

computer = []
index = random.randint(0, 49)
index2 = random.randint(0, 49)
while z:
    A = data[index]
    B = data[index2]

    print(logo)
    print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
    print(vs)
    print(f"Against: {B['name']}, {B['description']}, {B['country']}")
    
    user = input("Who has more followers? Type 'A' or 'B' ").lower()    
    
    if A['follower_count'] > B['follower_count']:
        if user == 'A'.lower():
            score += 1
            print(f"You are Right, Current score: {score}")
            
            if score >= 1:
                hold = index
                index2 = random.randint(0,49)
        elif user == "B".lower():
            print(f"Sorry that's Wrong, Your final score: {score}")
            
            z = False
    elif A['follower_count'] < B['follower_count']:
        if user == 'B'.lower():
            score += 1
            print(f"You are Right, Current score: {score}")
            if score >= 1:
                hold = index2
                index = random.randint(0, 49)
        elif user == 'A'.lower():
            print(f"You are Wrong, Your final score: {score}")
            z = False
            
           
