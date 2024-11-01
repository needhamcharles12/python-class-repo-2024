#!/usr/bin/env python3


def main():
   print("The Grade Software")
   grade_list = gathering_grades()
   press_enter1()
   removing_lowest_grade(grade_list)
   press_enter2()
   removing_random_grade(grade_list)
   press_enter3()
   edit_grade(grade_list)
   press_enter4()
   sorting_grades(grade_list)
   totaling_and_averaging(grade_list)
   credits()
   
   

def gathering_grades():
   grade_list = []
   grades = 0
   while grades != -1:
    grades = (int(input("Please enter the grade or -1 to stop: ")))
    if grades != -1: # -1 was getting appended to the list as well as ending the loop
      grade_list.append(grades)
      #print(grade_list)  test to see if appending is working
   print(grade_list)
   return grade_list

def press_enter1():
   enter = input("Please press ENTER to continue: ") 
   if enter == "":
      pass
   
def removing_lowest_grade(grade_list):
   print("Now removing lowest grade")
   #print(min(grade_list))
   lowest_grade = min(grade_list)
   #print(lowest_grade)
   lowest_index = grade_list.index(lowest_grade)
   #print(lowest_index)
   grade_list.pop(lowest_index)
   print(f"Lowest grade removed: {lowest_grade}")
   print(f"Updated grade list: {grade_list}")

def press_enter2():
   enter = input("Please press ENTER to continue: ") 
   if enter == "":
      pass 

def removing_random_grade(grade_list):
   print("Now removing random grade")
   import random
   random_grade = random.choice(grade_list)
   grade_list.remove(random_grade)
   print(f"Random grade removed: {random_grade}")
   print(f"Updated grade list: {grade_list}")

def press_enter3():
   enter = input("Please press ENTER to continue: ") 
   if enter == "":
      pass 

def edit_grade(grade_list):
   print("Please edit a grade")
   for index, grade in enumerate(grade_list):
      print(f"{index + 1}. {grade}")  #had to add +1 because it started at 0
   user_choice = int(input("Please select a grade to edit (type the front number): "))
   while user_choice > index + 1 or user_choice <= 0:
      print("Your choice is out of range!")
      user_choice = int(input("Please select a grade to edit (type the front number): "))
   new_grade = int(input("Enter the new grade: "))
   grade_list[user_choice - 1] = new_grade  #modifies the grade on the list
   print(f"Updated grade list: {grade_list}")

def press_enter4():
   enter = input("Please press ENTER to continue: ") 
   if enter == "":
      pass 

def sorting_grades(grade_list):
   print("Sorting and Reversing list")
   grade_list.sort()
   grade_list.reverse()
   print(f"Updated grade list: {grade_list}")

def totaling_and_averaging(grade_list):
   print("Now totaling and averaging grades")
   print(f"Total: {sum(grade_list)}")
   average = sum(grade_list) / len(grade_list)
   print(f"Average: {average}")
   
def credits():
   print("------------------------------------------------")
   print("Coded by Charles Needham")
    
if __name__ == "__main__":
    main() 