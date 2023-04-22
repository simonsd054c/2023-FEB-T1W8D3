from colored import fg, bg, attr

from todo_functions import add_todo, remove_todo, mark_todo, view_todo

print(f"{fg('blue')} {bg('yellow')}Welcome to your TODO List {attr('reset')}")

# CSV Structure
# title,completed
# Todo 1,False
# Todo 2,True
file_name = "list.csv"

# Check if list.csv exists
try:
    # In read mode, if the file doesn't exist, then, it throws exception
    todo_file = open(file_name, "r")

    # If it exists then all fine
    todo_file.close()
    print("In try block")
    
    # If it does not exists, then we can create it
except FileNotFoundError as e:
    todo_file = open(file_name, "w")
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")

def create_menu():
    print("1. Enter 1 to add a new item to your list")
    print("2. Enter 2 to remove item from your list")
    print("3. Enter 3 to mark an item as completed")
    print("4. Enter 4 to view your todo list")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice


user_choice = ""

while user_choice != "5":
    user_choice = create_menu()

    if (user_choice == "1"):
        add_todo(file_name)
    elif (user_choice == "2"):
        remove_todo(file_name)
    elif (user_choice == "3"):
        mark_todo(file_name)
    elif (user_choice == "4"):
        view_todo(file_name)
    elif (user_choice == "5"):
        continue
    else:
        print("Invalid Input")

    input("Press Enter to continue....")


print("Thank you for using todo list")