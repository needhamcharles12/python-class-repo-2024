#! /usr/bin/etc python3

## Code start! ##


print("Welcome to the Age Calculator!\n") # an introduction


## Variables ##
first_name = input("Please enter your first name: ") 
last_name = input("Please enter your last name: ")
current_year = int(input("Please enter the current year: " ))
birth_year = int(input("Please enter your birth year: "))

print("\n") # Just to create a new line

age = current_year - birth_year

print("Hello,", str(first_name), str(last_name) +"!\n" + "You are:", age, "years old!")
# The + is how you get the exclamation after the string without a space


print(f"Next year, you will be {age + 1}!") # F-string


print("\n")
print("--------------------------")
print("Written and created by Charles Needham")


