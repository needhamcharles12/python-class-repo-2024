#!/usr/bin/env python3


def main():
    display_title()
    game_over = False
    while game_over == False:
        weapon = show_choices()
        opponent_weapon = opponent_choice()
        fight_time()
        determine_winner(weapon, opponent_weapon)
        play_again = input("Do you want to play again? (y/n):   ").lower()
        if play_again != "y":
            game_over = True
    write_credits()

def display_title():
    print("Rock, Paper, Scissors!")
    print("-----------------------------------------")

def show_choices():
    while True:
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("")
        user_choice = int(input("Select your weapon! (1,2,3): "))

        if user_choice not in [1,2,3]:
            print("You need to pick 1-3!\n")
            continue

        if user_choice == 1:
            weapon = "Rock"
        elif user_choice == 2:
            weapon = "Paper"
        elif user_choice == 3:
            weapon = "Scissors"
            
        print(f"You have chosen: {weapon}!\n")
        return weapon
        

        
def opponent_choice():      
    from random import randrange
    opponent_roll = randrange(1, 4)
    
    if opponent_roll == 1:
        opponent_weapon = "Rock"
    elif opponent_roll == 2:
        opponent_weapon = "Paper"
    elif opponent_roll == 3:
        opponent_weapon = "Scissors"

    #print(f"{opponent_weapon}")    #test opponent weapon

    return opponent_weapon

def fight_time():

    enter = input("It's time to fight! Are you ready?! Press ENTER!:   ")
    if enter == "":
        pass

def determine_winner(weapon, opponent_weapon):
    if weapon == opponent_weapon:
        print(f"Looks like it's a tie! {weapon} vs. {opponent_weapon}! ")
    elif (weapon == "Rock" and opponent_weapon == "Scissors"
          or weapon == "Scissors" and opponent_weapon == "Paper"
          or weapon == "Paper" and opponent_weapon == "Rock"):
            print(f"You win! {weapon} beats {opponent_weapon}!")
    else:
        print(f"Oh no, you lose! {weapon} loses to {opponent_weapon}! ")

    print("")
    

def write_credits():
    print("------------------------------------------\n")
    print("Written by Charles Needham")



if __name__ == "__main__":
    main() 