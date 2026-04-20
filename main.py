import json


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
    key = f"project-{choice - 1}"
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

    return projectDetails, key


def editProject(
    projects, key, edit, change, file
):  # edit a item in the json depending on the users input
    match edit:
        case "title":
            projects[key]["Title"] = change
        case "desc":
            projects[key]["Description"] = change
        case "status":
            projects[key]["Status"] = change
        case "nextStep":
            projects[key]["Next Small Implementation"] = change
        case "tags":
            projects[key]["Tags"] = change
        case "notes":
            projects[key]["Notes"] = change
        case "changelog":
            projects[key]["Progress History"] = change
        case _:
            print("Invalid key.")

    updateFile(file, projects)


def updateFile(file, projects):  # Update the file then close
    with open(file, "w") as f:
        json.dump(projects, f, indent=4)
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

    try:
        projects = loadJson(file)
    except Exception as e:
        print(f"Failed to load {file}: {e}")
        return

    print(f"Loaded {file}\n")
    projectList = listProjects(projects)
    for i, title in enumerate(projectList, 1):
        print(f"{i}. {title}")

    # Type Security for initial choice
    while True:
        try:
            choice = int(input("Choose a Project to view its details: "))
        except ValueError:
            print("Invalid choice.")
            continue
        if choice < 1 or choice > len(projectList):
            print("Invalid choice.")
        else:
            break

    print("")

    # Prints the details of the project selected by the user
    selection = selectProject(choice, projectList, projects)
    for key, value in selection[0].items():
        print(f"{key}: {value}")

    while running:
        # Field that will be edited
        edit = input("Enter the key to edit: ")

        if edit == "exit":
            running = False
            break

        # Value that will be given to the field chosen above
        change = input("Enter the new value: ")
        key = selection[1]

        # Updates the json file with the new value
        editProject(projects, key, edit, change, file)

        # Fetches and prints all the new data
        selection = selectProject(choice, projectList, projects)
        for key, value in selection[0].items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
