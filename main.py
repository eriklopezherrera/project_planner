from os import system, name

def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    #Mac and Linux
    else:
        _ = system('clear')

def main_func():
    clear()
    switcher = {
        1: new_project,
        2: edit_project,
        3: view_project,
        4: exit_program
    }
    print("==========================================")
    print("|    Welcome to your project planner!    |")
    print("|                                        |")
    print("|                                        |")
    print("| 1)Add a new project                    |")
    print("| 2)Edit an existing project             |")
    print("| 3)View a project                       |")
    print("| 4)Exit                                 |")
    print("|                                        |")
    print("==========================================")
    option = input("Give me an option: ")
    func = switcher.get(int(option), "Invalid Option")
    func()

def new_project():
    clear()
    _ = input("Add a new project")
    main_func()
def edit_project():
    clear()
    _ = input("Edit existing project")
    main_func()
def view_project():
    clear()
    _ = input("View a Project")
    main_func()
def exit_program():
    clear()
    print("Goodbye")
    exit()

clear()
main_func()
