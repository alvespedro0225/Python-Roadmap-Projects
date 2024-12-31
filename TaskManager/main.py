#from pydantic import

from imports.FileManager import FileManager
from imports.Task import Task
from imports.InputValidator import InputValidator
from imports.AppLogic import AppLogic


if __name__ == "__main__":
    FileManager.get_file_data()
    Task.get_current_id()
    print(
        """
Choose an action. Possible:
add <description>,
update <id> <description> <mark*>,
delete <id>,
mark <id> <mark>,
list <mark*>,
clear,
reset,
quit

* = optional
marks = "todo", "ongoing", "completed"
        """
        )
    while True:

        while True:

            user_input = input()

            if not user_input:
                print(f"Invalid input \n{user_input}\n")
                continue

            argv = InputValidator.validate_input(user_input)
            
            if argv:
                break
        
        argc = len(argv)
        actions = {
            "add": AppLogic.add(argv, argc),
            "update": AppLogic.update(argv, argc),
            "delete": AppLogic.delete(argv, argc),
            "status": AppLogic.status(argv, argc),
            "list": AppLogic.list_tasks(argv, argc),
            "quit": AppLogic.quit_app(argv, argc),
            "clear": AppLogic.clear(argv, argc),
            "reset": AppLogic.clear(argv, argc)            
            }
        
        
