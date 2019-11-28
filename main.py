from os import system, name
import json

def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    #Mac and Linux
    else:
        _ = system('clear')

def new_project():
    #we need to get the latest index so that we can add another one
    with open('projects.json', 'r') as f:
        projects_dict = json.load(f)
        print("Size of the projects:")
        new = len(projects_dict)
        n_proj_name = input("Name of the project: ")
        n_descr = input("Description of the project: ")
        n_github = input("If you already have a github repo, paste it here: ")
        n_entry = {
            "project_id" : new,
            "project_name" : n_proj_name,
            "description" : n_descr,
            "github" : n_github,
            "status" : "initialized",
            "updates" : {"0":"Created project"},
            "percentage" : "0%"
            }
        with open('projects.json') as f:
            data = json.load(f)
        data.append(n_entry)
        with open('projects.json', 'w') as f:
            json.dump(data,f)

    _ = input("Project saved, press any key to return to the main menu")
    main_func()

def view_project(project):
    clear()
    for key,val in project.items():
        if str(key) != "updates":
            print(str(key) +"=>" + str(val))
        else:
            print("updates:")
            for up_id,up_desc in project['updates'].items():
                print("==" + up_desc)
    _ = input("Any key will return you to the projects view")
    view_projects()


def view_projects():
    clear()
    with open('projects.json', 'r') as f:
        projects_dict = json.load(f)
        print("==========================================")
        print("|             Projects                   |")
        print("|                                        |")
        print("==========================================")
        for project in projects_dict:
            print(str(project['project_id'] + 1) + " " + project['project_name'])
        print("0 Return to main menu")
        option = input("Select an option ")
        if option == "0":
            main_func()
        else :
            view_project(projects_dict[int(option)-1])
        _ = input("Press any key to return to the project selection")


def main_func():
    clear()
    switcher = {
        1: m_new_project,
        2: m_edit_project,
        3: m_view_project,
        0: m_exit_program
    }
    print("==========================================")
    print("|    Welcome to your project planner!    |")
    print("|                                        |")
    print("|                                        |")
    print("| 1)Add a new project                    |")
    print("| 2)Edit an existing project             |")
    print("| 3)View a project                       |")
    print("| 0)Exit                                 |")
    print("|                                        |")
    print("==========================================")
    option = input("Give me an option: ")
    func = switcher.get(int(option), "Invalid Option")
    func()

#Menu functions
def m_new_project():
    clear()
    new_project()
    main_func()
def m_edit_project():
    clear()
    _ = input("Edit existing project")
    main_func()
def m_view_project():
    view_projects()
    main_func()
def m_exit_program():
    clear()
    print("Goodbye")
    exit()

clear()
main_func()
