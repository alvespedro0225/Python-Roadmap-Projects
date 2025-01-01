import sys
from pydantic import BaseModel, validate_call

from .TaskManager import TaskManager
from .FileManager import FileManager
from .Task import Task


class AppLogic(BaseModel):

    @staticmethod
    @validate_call
    def add(argv: list[str], argc: int) -> None:

        description = argv[1]

        if argc >= 3:
            status = argv[2]
            TaskManager.add_task(description, status)

        else:
            TaskManager.add_task(description)

    @staticmethod
    @validate_call
    def update(argv: list[str], argc: int) -> None:

        description = argv[2]
        id = argv[1]
        try:
            id = int(id)
        except ValueError:
            print(f'"{argv[1]}" is not a valid number. Please try again.\n')
            return

        TaskManager.update_task(id, description)

    @staticmethod
    @validate_call
    def delete(argv: list[str], argc: int) -> None:

        id = argv[1]
        try:
            id = int(id)
        except ValueError:
            print(f'"{argv[1]}" is not a valid number. Please try again.\n')
            return

        TaskManager.delete_task(id)

    @staticmethod
    @validate_call
    def status(argv: list[str], argc: int) -> None:

        id = argv[1]
        status = argv[2]
        try:
            id = int(id)
        except ValueError:
            print(f'"{argv[1]}" is not a valid number. Please try again.\n')
            return

        TaskManager.update_status(id, status)

    @staticmethod
    @validate_call
    def list_tasks(argv: list[str], argc: int) -> None:
        if argc <= 1 or argv[1] not in TaskManager.possible_status:
            tasks = TaskManager.task_list
            for task in tasks:
                print(task)
            print()
        else:

            filter_condition = argv[1]
            tasks = TaskManager.filter_task(
                lambda task: task.status == filter_condition
            )
            for task in tasks:
                print(task)
            print()

    @staticmethod
    @validate_call
    def quit_app(argv: list[str], argc: int) -> None:
        FileManager.write_to_file()
        Task.write_current_id()
        sys.exit()

    @staticmethod
    @validate_call
    def clear(argv: list[str], argc: int) -> None:

        TaskManager.clear()

    @staticmethod
    @validate_call
    def reset(argv: list[str], argc: int) -> None:

        TaskManager.clear(reset=True)
