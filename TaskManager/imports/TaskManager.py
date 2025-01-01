from pydantic import BaseModel, validate_call
from typing import ClassVar, Callable, overload

from .Task import Task
from .Utils import get_current_time


class TaskManager(BaseModel):

    task_list: ClassVar[list[Task]] = []
    possible_status: ClassVar[list[str]] = ["todo", "ongoing", "completed"]

    @classmethod
    @validate_call
    @overload
    def add_task(cls, task_or_description: str, status: str = "todo") -> None: ...

    @overload
    @classmethod
    @validate_call
    def add_task(cls, task_or_description: Task, status: str = "todo") -> None: ...

    @classmethod
    @validate_call
    def add_task(cls, task_or_description, status="todo") -> None:
        if isinstance(task_or_description, Task):
            cls.task_list.append(task_or_description)
        else:
            if status in cls.possible_status:
                task = Task(description=task_or_description, status=status)
                cls.task_list.append(task)
                print(
                    f'Added new task with description "{task.description}", status {task.status} and ID {task.id}.\n'
                )
            else:
                print(
                    f'Status "{status}" is not a valid status. Valid: {cls.possible_status}\n'
                )

    @classmethod
    @validate_call
    def update_task(cls, id: int, description: str) -> None:
        task = cls.filter_task(lambda task: task.id == id)[0]
        task.description = description
        task.updated_at = get_current_time()
        print(f'Updated task {id} to "{task.description}".\n')

    @classmethod
    @validate_call
    def delete_task(cls, id: int) -> None:
        task = cls.filter_task(lambda task: task.id == id)[0]
        cls.task_list.remove(task)
        print(f"Deleted task {id}.\n")

    @classmethod
    @validate_call
    def update_status(cls, id: int, status: str) -> None:
        task = cls.filter_task(lambda task: task.id == id)[0]
        status = status.lower()

        if status not in cls.possible_status:
            print(f'Invalid status "{status}."\n')
            return

        task.status = status
        task.updated_at = get_current_time()
        print(f'Updated task {id} to "{task.status}".\n')

    @classmethod
    @validate_call
    def clear(cls, reset: bool = False) -> None:
        cls.task_list = []
        if reset:
            Task.reset()
            print("App data has been reset.\n")
        else:
            print("All tasks have been cleared.\n")

    @classmethod
    @validate_call
    def filter_task(cls, filter_condition: Callable[[Task], bool]) -> list[Task]:
        return list(filter(filter_condition, cls.task_list))
