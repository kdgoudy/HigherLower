from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account_a["name"]
    account_descr = account_a["description"]
    account_country = account_a["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and return if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

#Display art
print(logo)
score = 0
game_should_continue = True

#Generate a random account from the game data.
account_b = random.choice(data)

#Make game repeatable
while game_should_continue:

#Making account at position B become the account in position A
    account_a = account_b
    account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare A: {format_data(account_b)}")

#Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#Check if user is correct
#Get follower count of each account

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

#Clear the screen between rounds
    clear()
    print(logo)

#Give user feedback on their guess
#Score keeping
    if is_correct:
        score += 1
        print("You're right Current score: {score}")
    else:
        game_should_continue = False
        print("Sorry, that's wrong. Final score: {score}")



