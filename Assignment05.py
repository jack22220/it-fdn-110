# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JJohanneson , 11/15/23, Completed Assignment
# ------------------------------------------------------------------------------------------ #
import json
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # dictionary of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
parts = list[str]


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students =json.load(file)
    file.close()

except FileNotFoundError as e: #error if file is not found
        print('We could not find that file!')
        print('----------Robot says----------')
        print(e,e.__doc__,type(e),sep='\n') #documentation

except Exception as e: #all other errors
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')#documentation
finally:
    if file.closed == False: #protect file from being left open
        file.close()
print(students)


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha(): #check if the name is only letters
                    raise ValueError("The first name should not contain numbers") #error if non letters in name

            except ValueError as e:
                print(e)  # Prints the custom message
                print("-- Technical Error Message -- ")
                print(e.__doc__)
                print(e.__str__())

            try:
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha(): #check if the name is only letters
                    raise ValueError("The last name should not contain numbers") #error if non letters in name

            except ValueError as e:
                print(e)  # Prints the custom message
                print("-- Technical Error Message -- ")                             
                print(e.__doc__)
                print(e.__str__())

            except Exception as e:
                print("There was an error!\n")
                print("Built-In Python error info: ")
                print(e, e.__doc__, type(e), sep='\n')

            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)

            print('-'*50)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            print('-'*50)

            continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for row in students:
            print(f"{row["FirstName"]} {row["LastName"]} is enrolled for {row["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        
        try:
            file = open(FILE_NAME, "w")

        except FileNotFoundError as e: 
            if file.closed == False: # Make sure the file is open before trying to close it.
                file.close()
            print("Text file must exist before running this script!]\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            if file.closed == False: # Make sure the file is open before trying to close it.
                file.close()
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')


        json.dump(students, file)  #put students data into 'file'
        file.close() #close file
        print("The following data was saved to file!") #show what was added to the file

        for student in students:
            print(f"Student {student_first_name} {student_last_name} for {course_name}")
        continue


    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

