# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   PNguyen,5/21/2025,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = ("---- Course Registration Program ----.\nSelect from the following menu:.\n1. Register a Student for a Course..\n"
             "2. Show current data.\n3. Save data to a file.\n4. Exit the program.\n----------------------------------------- ")

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data in json
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    print(type(file))
    students = json.load(file)
    file.close()
except Exception as e:
    print("Error: There was a problem with reading the file.")
    print("Please check that the file exists and that it is in a json format.")
    print("--Technical Error Message--")
    print(e.__doc__)
    print(e.__str__())
    file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")

            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                (f'Student {student["FirstName"]} '
                    f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
