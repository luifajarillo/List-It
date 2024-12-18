import os
from datetime import datetime

if not os.path.exists("Notes"):
    os.makedirs("Notes")

def line():
    for i in range(23):
        print("-", end="")
    print()

def new_note(filename):
    try:
        open(f"Notes\\{filename}.txt", "x")
        print(f"{filename} created successfully!")
    except:
        print("Note already exists.")

def view_notes():
    global list_of_notes
    global index
    list_of_notes = os.listdir("Notes")

    for number, notes in enumerate(list_of_notes):
        note = notes.replace(".txt", "")
        print(f"{number+1}. {note}")
    try:
        index = int(input("Choose a note: "))
    except:
        print("Input must be a number.")
        return
    if index > len(list_of_notes):
        print(f"Error. There are only {len(list_of_notes)} notes.")
        return False
    chosen_note = list_of_notes[index-1].replace(".txt", "")
    print(f"\n{chosen_note}:")
    file = open(f"Notes\\{list_of_notes[index-1]}", "r+")
    content = file.readlines()

    for number, tasks in enumerate(content):
        print(f"{number+1}. {tasks.strip()}")

def time_remaining():
    if view_notes() == False:
        return

    try:
        due_date = input("Due date (YYYY-MM-DD HH:MM:SS): ")
        due_date = datetime.strptime(due_date, "%Y-%m-%d %H:%M:%S")
        remaining = due_date - datetime.now()
        days, seconds = remaining.days, remaining.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes")
    except:
        print("Invalid format, please try again.")

def edit_notes():
    print()
    line()
    print("Notes:")
    view_notes()

    file = open(f"Notes\\{list_of_notes[index-1]}", "r+")
    content = file.readlines()

    edit = input("\nEdit note? [Y/N]: ").upper()

    if edit == 'Y':
        print("\n1. Add a task\n2. Mark a task")
        choice = input("Choose an option: ")

        if choice == '1':
            new_task = input("Task: ")
            file.write(f"{new_task} - ")
            due_date = input("Due date (YYYY-MM-DD HH:MM:SS): ")
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d %H:%M:%S")
                file.write(f"Due on {due_date.strftime('%B %d %Y %H:%M:%S')}\n")
                print("Task added successfully!")
            except:
                print("Invalid input, please try again.")
        elif choice == '2':
            task = int(input("Task: "))
            try:
                del content[task-1]
                print("Task marked successfully!")
                with open(f"Notes\\{list_of_notes[index-1]}", "w") as file:
                    for i in content:
                        file.write(i)
            except:
                print("There are currently no tasks in this note.")
        else:
            print("Invalid option.")
            return
    elif edit == 'N':
        pass

def delete_note():
    list_of_notes = os.listdir("Notes")

    for number, notes in enumerate(list_of_notes):
        note = notes.replace(".txt", "")
        print(f"{number+1}. {note}")

    filename = input("Enter note name: ")
    filenameog = (filename + ".txt")

    if filenameog in os.listdir("Notes"):
        os.remove(f"Notes\\{filenameog}")
        note = filename.replace(".txt", "")
        print(f"{note} deleted successfully!")
    else:
        print("Note does not exist.")

def main():
    print("Welcome to List It!")

    while True:
        print()
        line()
        print("What do you want to do?")
        print("1. Create a new note\n2. View notes\n3. Edit notes\n4. Calculate time remaining\n5. Delete a note\n6. Exit")

        choice = input("Enter an option: ")

        if choice == '1':
            filename = input("Enter note name: ")
            new_note(filename)
        elif choice == '2':
            print()
            line()
            print("Notes:")
            view_notes()
        elif choice == '3':
            edit_notes()
        elif choice == '4':
            time_remaining()
        elif choice == '5':
            delete_note()
        elif choice == '6':
            print("Exiting the program… thank you for using List It!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__" :
    main()
