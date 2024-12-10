#!/usr/bin/env python3

from datetime import date, datetime
import csv

def reading_file(budget_list):
    with open("exam_3_test_file.txt", "r") as f: #with open closes file automatically
        for line in f:
            if line:
                budget_list.append(line.strip().split("|")) #imports data in .txt and converts to string format while appending to list

def display_budget(budget_list):
    print(f"{"Month:":20} {"Amount:":30}") #string spacing
    for index, budget in enumerate(budget_list):
        print(f"{budget[0]:20} {budget[1]:30}")

def display_budget_index(budget_list):  #numbered list
    print(f"{"Month:":20} {"Amount:":30}")
    for index, budget in enumerate(budget_list):
        print(f"{index+1}. {budget[0]:20} {budget[1]:30}")

def creating_output_file(budget_list):
    print("")
    filename = input("Please enter a name for the file: ")
    with open(f"{filename}.csv", "w", newline="") as f: #w writes to file
        writer = csv.writer(f)
        writer.writerows(budget_list)
    print(f"{filename}.csv was created successfully.")

def editing_list(budget_list):
    print("")
    display_budget_index(budget_list)
    while True:
        try:
            user_choice = int(input("Please enter the month you wish to edit or 0 to exit: ")) - 1 #minus 1 for index value
            if user_choice == -1:
                break
            if user_choice < 0 or user_choice > len(budget_list) - 1:
                raise ValueError("Please choose a valid option.")
            print(f"{budget_list[user_choice][0]} current value: {budget_list[user_choice][1]}")
            new_value = float(input("Please enter the new value: "))
            budget_list[user_choice][1] = str(new_value) #str to convert the float back into string like the rest
            print(f"\n{budget_list[user_choice][0]} updated to: {new_value:.2f}\n")
            break       
        except Exception as e:
            print(f"\nError Occurred!: {e}")
            display_budget_index(budget_list)


def deleting_value(budget_list):
    print("")
    display_budget_index(budget_list)
    while True:
        try:
            user_choice = int(input("Please enter the month you wish to remove or 0 to exit: ")) - 1
            if user_choice == -1:
                break
            if user_choice < 0 or user_choice > len(budget_list) - 1:
                raise ValueError("Please choose a valid option.")
            
            print(f"Are you sure you want to remove {budget_list[user_choice][0]}?")

            decision = (input("Type y to continue or n to exit: ")).lower() #lower to lowercase choice
            if decision == "y":
                print(f"Removing {budget_list[user_choice][0]}\n")
                del budget_list[user_choice]
                break
            elif decision == "n":
                print("No changes made.\n")
                break
            else:
                raise ValueError("Please type y or n.")
        except Exception as e:
            print(f"\nError Occurred!: {e}")
            

def printing_ending_time():
    ending_time = datetime.now()
    ending_time = ending_time.strftime("%B %d, %Y %I:%M:%S %p") #formats datetime
    print(f"\nEnding time: {ending_time}")


def main():
    print("Budget Editor Program")
    today = datetime.now()
    today = today.strftime("%B %d, %Y %I:%M:%S %p")
    print(f"Starting time: {today}")
    print("=============================================\n")
    budget_list = []
    reading_file(budget_list)
    #print(budget_list) was making sure the list acutally worked
    display_budget(budget_list)
    while True:
        try:
            print("")
            print("Choose an option.")
            print("1 - Edit a value")
            print("2 - Delete a value")
            print("3 - Write current data to .csv and end program")
            print("0 - Close program without operating")
            user_choice = int(input("Enter your selection: "))
            if user_choice == 1:
                editing_list(budget_list)
            elif user_choice == 2:
                deleting_value(budget_list)
            elif user_choice == 3:
                creating_output_file(budget_list)
                break
            elif user_choice == 0:
                break
            else:
                raise ValueError("Please choose a valid option.")

            display_budget(budget_list)
        except Exception as e:
            print(f"\nError Occurred!: {e}")

    printing_ending_time()
    print("\n=============================================")
    print("Coded by Charles Needham")

if __name__ == "__main__":
    main()  
