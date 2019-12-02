from os import system, name, path
import json

def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    #Mac and Linux
    else:
        _ = system('clear')
def init_app():
    if path.exists('projects.json') is False:
        print('File is not present. Creating the file...')
        data = []
        with open('projects.json', 'w') as file:
            json.dump(data,file)
        _ = input('Create the file?')
def edit_projects():
    #We need to know which entry to edit
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
            edit_project(projects_dict[int(option)-1])
        _ = input("Press any key to return to the project selection")

def edit_project(project):
    clear()
    print("==========================================")
    print("|             Edit Project               |")
    print("|                                        |")
    print("==========================================")
    print("1)Edit name (" + project['project_name'] + ")")
    print("2)Edit description (" + project['description'] +")" )
    print("3)Edit github repository (" + project['github'] +")" )
    print("4)Edit status (" + project['status'] +")" )
    print("5)Add update (" + str(len(project['updates'])) +" Updates)" )
    print("6)Edit Percentage (" + project['percentage'] +")" )
    print("7)Save changes ")
    print("8)Quit without saving ")
    print("0)Return to previous menu ")
    e_switcher = {
        1: edit_name,
        2: edit_descr,
        3: edit_github,
        4: edit_status,
        5: add_update,
        6: edit_percentage,
        7: edit_save,
        8: edit_quit,
        0: edit_return
    }
    option = input("Select an option: ")
    e_func = e_switcher.get(int(option), "Invalid Option")
    clear()
    e_func(project)
    main_func()
def edit_name(project):
    print('Current name: ' + project['project_name'])
    e_name = input('Enter new name: ')
    project['project_name'] = e_name
    edit_project(project)
def edit_descr(project):
    print('Current description: ' + project['description'])
    e_desc = input('Enter new description: ')
    project['description'] = e_desc
    edit_project(project)
def edit_github(project):
    print('Current github: ' + project['github'])
    e_github = input('Enter new github: ')
    project['github'] = e_github
    edit_project(project)
def edit_status(project):
    print('Current status: ' + project['status'])
    e_status = input('Enter new status: ')
    project['status'] = e_status
    edit_project(project)
def add_update(project):
    max_update_id = len(project['updates'])
    print(max_update_id)
    new_update = input('Type your update here: ')
    new_up_dict = {
        str(max_update_id + 1) : new_update
    }
    project['updates'][str(max_update_id)] = new_update
    #print(type(project['updates']))
    print(project['updates'])
    _ = input('press any key to return to edit menu')
    edit_project(project)
def edit_percentage(project):
    print('Current percentage: ' + project['percentage'])
    e_percentage = input('Enter new percentage: ')
    project['percentage'] = e_percentage
    edit_project(project)
def edit_save(project):
    with open('projects.json', 'r') as f:
        projects_dict = json.load(f)
        print("edit project id: " + str(project['project_id']))
        #since the position will always match the id (id 0 will be position 0)
        #we can safely user the id as the position for the edit/save process
        projects_dict[project['project_id']] = project
        print(projects_dict[project['project_id']])
        with open('projects.json', 'w') as f:
            json.dump(projects_dict,f)
    _ = input('Changes have been saved, press any key to continue')
    edit_project(project)
def edit_quit(project):
    print("Skipping changes and returning")
    edit_projects()
def edit_return(project = None):
    edit_projects()

def new_project():
    #we need to get the latest index so that we can add another one
    with open('projects.json', 'r') as f:
        projects_dict = json.load(f)
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
    switcher = {
        1: m_new_project,
        2: m_edit_project,
        3: m_view_project,
        0: m_exit_program
    }
    func = switcher.get(int(option), "Invalid Option")
    func()

#Menu functions
def m_new_project():
    clear()
    new_project()
    main_func()
def m_edit_project():
    clear()
    edit_projects()
    main_func()
def m_view_project():
    view_projects()
    main_func()
def m_exit_program():
    clear()
    print("Goodbye")
    exit()

clear()
init_app()
main_func()
