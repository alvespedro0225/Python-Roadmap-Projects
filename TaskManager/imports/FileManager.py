from pydantic import BaseModel
from pathlib import Path
from typing import ClassVar
import json

from .Task import Task
from .TaskManager import TaskManager


class FileManager(BaseModel):

    FILE_PATH: ClassVar[Path] = Path(__file__).parent / "tasks.json"
    ID_PATH: ClassVar[Path] = Path(__file__).parent / "id.txt"

    @classmethod
    def get_file_data(cls) -> None:
        try:
            with open(cls.FILE_PATH, "r") as file:
                data = json.load(file)
                if data:
                    for task_json in data:
                        task = Task(
                            description=task_json["description"],
                            status=task_json["status"],
                            id=task_json["id"],
                            created_at=task_json["created_at"],
                            updated_at=task_json["updated_at"],
                        )
                        TaskManager.add_task(task)

        except FileNotFoundError:
            with open(cls.FILE_PATH, "w") as file:
                file.write("")

        except json.decoder.JSONDecodeError:
            pass

    @classmethod
    def write_to_file(cls) -> None:
        with open(cls.FILE_PATH, "w") as file:
            file.write("[")
            tasks = TaskManager.task_list
            for task in tasks:
                file.write(task.to_JSON())
                if task != tasks[-1]:
                    file.write(",")
            file.write("]")
