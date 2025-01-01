# from pydantic import

from imports.FileManager import FileManager
from imports.Task import Task
from imports.InputValidator import InputValidator
from imports.AppLogic import AppLogic


if __name__ == "__main__":
    Task.get_task_id()
    FileManager.get_file_data()
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
            "add": AppLogic.add,
            "update": AppLogic.update,
            "delete": AppLogic.delete,
            "status": AppLogic.status,
            "list": AppLogic.list_tasks,
            "quit": AppLogic.quit_app,
            "clear": AppLogic.clear,
            "reset": AppLogic.reset,
        }

        try:
            action = actions[argv[0]]
            action(argv, argc)
        except KeyError:
            print(f'Wrong arguments provided "{argv[0]}".\n')
        except IndexError:
            word = ""
            for index in range(argc):
                word += argv[index]
                if index < argc:
                    word += ", "
            print(f'Missing arguments, please try again. Passed "{word}".\n')
