#!/usr/bin/env python3

def main():
    print("Welcome to the content manager application")
    program_on = True
    while program_on == True:
        import csv
        print("-------------------------------------------------\n")
        print("Choose an option.")
        print("1 - Create a new contact file")
        print("2 - Add a new contact")
        print("3 - View all contacts")
        print("4 - Modify an Existing contract")
        print("5 - Save and exit")
        user_choice = int(input("Enter your selection: "))
        while user_choice > 5 or user_choice < 0:
            print("Invalid option. Please try again.")
            user_choice = int(input("Enter your selection: "))
        print("-------------------------------------------------\n")
        if user_choice == 1: 
            creating_file()
        elif user_choice == 2:
            adding_contacts()
        elif user_choice == 5:
            print("Goodbye!")
            program_on = False
            




def creating_file():
    with open("contacts.csv", "w") as f:
        print("Contact file created!")

def adding_contacts(csv):
    with open("contacts.csv", "w") as f:
        writer = csv.writer(f)









if __name__ == "__main__":
    main()  