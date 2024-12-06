#!/usr/bin/env python3

import locale as lc

def main():
    print("Simple Budget Tracker")
    print("--------------------------------------")
    user_income = obtaining_income()
    print("--------------------------------------")
    total_expenses, expense_list = obtaining_expenses()
    printing_budget(user_income, total_expenses)
    print("\nComplete Expense List")
    print("--------------------------------------")
    looping_expenses(expense_list)
    print("--------------------------------------")
    print("Coded by Charles Needham")

def obtaining_income():
    while True:
        try:
            user_income = (input("Please enter your income: $"))
            user_income = float(user_income)
            while user_income < 0:
                print("Invalid input! Amount cannot be less than 0!")
                user_income = (input("Please enter your income: $"))
                user_income = float(user_income)
            print(f"Your total income is ${user_income:.2f}")
            break
        except ValueError:
            print("Invalid input. Please type a number")
    return user_income

def obtaining_expenses():
    obtaining = True
    expense_list = []
    while obtaining == True:
        try:
            user_expenses = float(input("Please enter an expense amount or 0 to quit: $"))
            while user_expenses < 0:
                print("Invalid input! Amount cannot be less than 0!")
                user_expenses = float(input("Please enter an expense amount or 0 to quit: $"))
            if user_expenses == 0:
                obtaining = False
            else:
                user_expenses = float(user_expenses)
                expense_list.append(user_expenses)
        except ValueError:
            print("Invalid input. Please type a number")
    total_expenses = sum(expense_list)
    return total_expenses, expense_list
    #print(expense_list)

def printing_budget(user_income, total_expenses):
    print("\n Budget Results:")
    print("--------------------------------------")
    print(f"Total income: ${user_income:.2f}")
    (print(f"Total expenses: ${total_expenses:.2f}"))
    budget = user_income - total_expenses
    print(f"Remaining Budget: ${budget:.2f}")

def looping_expenses(expense_list):
    lc.setlocale(lc.LC_ALL, "en_US")
    for index, expense in enumerate(expense_list, start=1):
        us_expense = lc.currency(expense, grouping = True)
        print(f"{index}. {us_expense}")
        
    
if __name__ == "__main__":
    main()  