#!/usr/bin/env python3

def main():
    print("STRING REPLACEMENT TOOL")
    print("--------------------------------------------------------------------------")
    userString, subString = obtainingInput()
    print("\nNow searching for substring within the main string, please wait!")
    print("--------------------------------------------------------------------------")
    indexValue = searchingSubstring(userString, subString)
    print("--------------------------------------------------------------------------")
    replacingString(userString, subString, indexValue)
    print("\nThank you for using the program!")
    print("--------------------------------------------------------------------------")
    print("Coded by Charles Needham")


def obtainingInput():
    while True:
        try:    
            userString = input("Plese enter the string to search through: ")
            if userString.isnumeric():
                raise ValueError("Input must be a string!")
            subString = input("Please enter the string to search for: ")
            if subString.isnumeric():
                raise ValueError("Input must be a string!")
            return userString, subString
        except ValueError as e:
            print (f"Error: {e}.")


def searchingSubstring(userString, subString):
    if subString in userString:
        indexValue = userString.find(subString)
        #print(userString.find(subString))
        print(f"{subString} was found at index {indexValue}")
    else:
        print("Substring not found!")
        indexValue = -1
    return indexValue

def replacingString(userString, subString, indexValue):
    while indexValue != -1:
        userChoice = input(f"Would you like to replace {subString} for something else? (y/n): ")
        if userChoice.lower() == "n":
            print("No replacement was made.")
            break
        else:
            try:
                replacementString = input(f"Please enter a replacement string: ")
                if replacementString.isnumeric():
                    raise ValueError("Input must be a string!")
                userString.replace(subString, replacementString)
                print(f"Your new string is: {userString.replace(subString, replacementString)}.")
                break
            except ValueError as e:
                print (f"Error: {e}.")

if __name__ == "__main__":
    main()  