from game_data import data
from replit import clear
import random
import art
score = 0
not_continue = True
# print(art.logo)
while not_continue:
    print(art.logo)
    _ = random.randint(0,len(data)-1)
    new_list = data.pop(_)
    a = data[_]['follower_count']
    
    print(f"Compare A: {data[_]['name']}, a {data[_]['description']}, from {data[_]['country']}.\n{art.vs}")
    
    _ = random.randint(0,len(data)-1)
    new_list = data.pop(_)
    b = data[_]['follower_count']
    
    print(f"Against B: {data[_]['name']}, a {data[_]['description']}, from {data[_]['country']}.")
    
    choice = input('who has more followers? type \'A\' or \'B\' ').lower()
    
    if a > b and choice == 'a':
        score += 1
        clear()
        print(f"you are right! score = {score}.")
    elif b > a and choice == 'b':
        score += 1
        clear()
        print(f"you are right! score = {score}.")
    else:
        not_continue = False