from art import logo,vs
from game_data import data
import random



def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take the user guess and follower counts of a and b and returns if they got it right"""
    if a_followers > b_followers:
        if user_guess == "a":
          return True
        else:
            return False
    if b_followers > a_followers:
        if user_guess =="b":
            return True
        else:
            return False

"""Alternatively: if a_followers >b_followers: return user_guess == 'a' else: return user_guess == 'b'"""


print(logo)
score = 0
game_should_continue =True
account_b = random.choice(data)

#while loop to make game repeatable
while game_should_continue:
    #Generate a random account from the game data

    # Making account at position B become the next account at position A when user gets guess right.

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    """this basically says that if the random choice for account a and b are the same then another random account should be picked for account b"""

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    #Ask user for their guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear the screen
    print("\n" *20)
    print(logo)

    #Check if user got it right, get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct =check_answer(guess, a_follower_count, b_follower_count)


    #Give user feedback on their game
    if is_correct:
        score += 1
        print(f"You're right! good job. Current score is {score}")
    else:
        print(f"Womp Womp, you're wrong. Final score is {score}")
        game_should_continue = False



