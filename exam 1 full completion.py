#!/usr/bin/env python3

while True:    # to loop the game back to the beginning
      
    print("")
    print("Welcome to the Number Guesser!")

    print("Guess the random number in 10 tries! (integers only 0-100)")
    print("")

    user_guess = int(input("Please guess your number!:     "))

    counter = 1

                
    from random import randrange

    random_number = randrange(0, 100)

    # following is just for testing purposes make sure new random number each game
    #print(f"The random number is !: {random_number} ")  

    max_guess = 10

    while user_guess != random_number:     # print statements based off if the user guess is less or more than the random number
        print("Sorry that is incorrect.")
        if random_number > user_guess:
            print(f"Your guess of {user_guess} was smaller than the number\n")
        if random_number < user_guess:
            print(f"Your guess of {user_guess} was larger than the number\n")

        counter += 1
        user_guess= int(input(f"Let's try again! Try #{counter}:       "))   # counter is added up
        if max_guess == counter:                                        # fail state
            print("Sorry you reached your max guesses! Game Over!")
            break               # breaks the while loop

    if user_guess == random_number:
            print("You got it! Congrats!")

    play_again = input("Would you like to play again? (y/n): ").lower()   # lower makes whatever the user types lowercase
    if play_again == "y":
        from random import randrange   # makes sure to give you a new number

        random_number = randrange(0, 100)
        continue                # loop starts at beginning

    elif play_again != "y":
        print("\nThank you for playing!")
        break

      
print("--------------------------------------------")
print("Code by Charles Needham")