#!/usr/bin/env python3

def main():
    print("WcDonalds Employees Organization Log")
    print("==================================================\n")

    employee_list = []    #declaring lists
    employee_ids = []

    employees = int(input("How many users are you adding?: "))
    while employees <= 0:    #user input check
        print("Please enter a number higher than 0\n")
        employees = int(input("How many employees are you adding?: "))
        
    print("\n==================================================")
    
    creating_employees(employees, employee_list) #employee list filled
    creating_ids(employee_ids, employees)  #employee ids filled
    employee_dict = creating_dictionaries(employee_list, employee_ids)  #employee list and ids made into dictionary

    creating_user_info(employee_dict)  #outputs employee names and ids

    
    print("\n==================================================")
    print("Coded by Charles Needham")
        
    

def creating_employees(employees, employee_list):
    i = 0
    for i in range(i,employees):   #for loop iterates until it reaches user input 
        while True:  #needed a way to loop back to input while having the constraint
            new_employee = input("Please type in the name of the new employee: ").lower().title() #makes user input all lower and then capitalizes first word
            if new_employee not in employee_list:
                employee_list.append(new_employee)  #adds name to the end of the list
                print("\n==================================================")
                i += 1
                break
            else: 
                print("Error! Name is already in database!")
    
    #print(employee_list)  test code

def creating_ids(employee_ids, employees):
    from random import randrange
    employee_number = randrange(1, 500)
    x = 0
    for x in range(x, employees):   #for loop iterates until it reaches user input 
        while True:
            if employee_number not in employee_ids:    #makes sure not to give out duplicate ids
                employee_ids.append(employee_number)  #adds id to the end of the list
                x += 1
                employee_number = randrange(1, 500)
                break
            else:
                employee_number = randrange(1, 500)  #rolls a random number again
                continue
    #print(employee_ids)  test code

def creating_dictionaries(employee_list, employee_ids):
    employee_dict = {name: id for name, id in zip(employee_list, employee_ids)}  #for loop that iterates dictionary over the lists with zip iterating both lists in unison
    #print(employee_dict)  test code
    return employee_dict 

def creating_user_info(employee_dict):
    print("\nCreated User Information")
    for name, id in employee_dict.items():  #.items returns the key value pairs of the dictionary
        print("==================================================")
        print(f"Employee name: {name}")
        print(f"Employee ID: {id}")
    
    
if __name__ == "__main__":
    main()