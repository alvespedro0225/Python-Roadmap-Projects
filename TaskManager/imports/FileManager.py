from pydantic import BaseModel
from pathlib import Path
from typing import ClassVar
import json

from .Task import Task
from .TaskManager import TaskManager

class FileManager(BaseModel):

    FILE_PATH:ClassVar[Path] = Path(__file__).parent / "tasks.json"

    
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
                            _created_at=task_json["_created_at"],
                            updated_at = task_json["updated_at"]
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
            for task in TaskManager.task_list:
                json.dump(task, file)
            file.write("]")