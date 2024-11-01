#!/usr/bin/env python3


def main():
    student_dict = creating_dictionary()
    listing_students(student_dict)
    accessing_student_info(student_dict)
    removing_student(student_dict)
    accessing_gpa(student_dict)
    clearing_registry(student_dict)
    credits()
    

def creating_dictionary():
    student_dict = {
        "Dave": {
            "ID": "1",
            "GPA": "3.1",
            "Credits completed": "97",
            "Grades": "[87, 96, 74, 100]",
        }
}
    
    student_dict["Sandy"] = {
        "ID": "2",
        "GPA": "3.8",
        "Credits completed": "120",
        "Grades": "[90, 95, 95, 100]"

    }


    print(student_dict)
    print("\n")

    return student_dict



def listing_students(student_dict):
    print("List of Students\n")

    for student in student_dict:
        print(student)

def accessing_student_info(student_dict):
    print("\n")
    print("Student ID\t GPA\t Credits Completed\t Grades")
    for x, stuff in student_dict.items():
        print(f"{x}\t{stuff["ID"]}\t {stuff["GPA"]}\t\t {stuff["Credits completed"]}\t\t {stuff["Grades"]}")

    print("")


    print("Accessing student information using the key in a loop:")
    for key in student_dict:
        print(key, student_dict[key])

    print("")

def removing_student(student_dict):
    print("Dave has dropped the course, removing student from registry")
    (student_dict.pop("Dave"))
    print(student_dict)
    print("")

def accessing_gpa(student_dict):
    print("Acquiring Sandy's GPA")
    print(student_dict["Sandy"]["GPA"])
    print("")

def clearing_registry(student_dict):
    print("Students have graduated. Clearing registry...")
    student_dict.clear()
    print(student_dict)

def credits():
    print("-----------------------------------------------------------------------------")
    print("Coded by Charles Needham")

    

if __name__ == "__main__":
    main()