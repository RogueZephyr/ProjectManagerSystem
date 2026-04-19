import json

debug = False


def loadJson(filename):
    with open(filename, "r") as file:
        return json.load(file)


def listProjects(projects):
    projectList = []

    for project in projects:
        title = projects[project]["Title"]
        projectList.append(title)

    return projectList


def selectProject(
    choice, projectsList, projects
):  # Prints a Menu for the users chosen project
    key = f"project-{choice}"
    project = projects[key]

    projectDetails = {
        "key": key,
        "title": project["Title"],
        "description": project["Description"],
        "status": project["Status"],
        "last_updated": project["Last Updated"],
        "next_small_implementation": project["Next Small Implementation"],
        "tags": project["Tags"],
        "notes": project["Notes"],
        "progress_history": project["Progress History"],
    }

    return projectDetails


def editProject(
    projectDetails, key, change
):  # edit a item in the json depending on the users input
    projectDetails[key] = change
    return projectDetails

def updateFile(file): # Update the file then close
    
    return

def deleteProject():
    # Moves a project from the Json file to a temporary archive
    return


def createProject():
    # Prompts the user to create a title, desc, possible tags and a initial setup or feature plan
    return


def main():
    running = True
    print("Welcome to the Project Manager.")

    file = "projects_Sample.json"
    projects = loadJson(file)
    if projects == None:
        print("project failed to load!")
    print(f"Loaded {file}\n")
    projectList = listProjects(projects)
    for i, title in enumerate(projectList, 1):
        print(f"{i}. {title}")

    choice = 1 - int(input("Choose a Project to view its details: "))
    print("")

    selection = selectProject(choice, projectList, projects)
    for key, value in selection.items():
        print(f"{key}: {value}")

    while running:
        edit = input("Enter the key to edit: ")

        if edit == "exit":
            running = False
            with open(file, "w") as update:
                json.dump(projects, update)
            break
        change = input("Enter the new value: ")
        editProject(selection, edit, change)
        for key, value in selection.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
