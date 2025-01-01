from pydantic import BaseModel
from typing import ClassVar, Optional
from pathlib import Path
import json

from .Utils import get_current_time

class Task(BaseModel):


    FILE_PATH:ClassVar[Path] = Path(__file__).parent / "id.txt"
    _current_id:ClassVar[int]
    id:Optional[int] = None
    created_at:str = get_current_time()
    updated_at:str = get_current_time()
    status:str
    description:str
    

    def __init__(self, description, status, **kwargs) -> None:
        super().__init__(
            description = description,
            status = status,
            **kwargs
            )
        if not self.id:
            self.id = self.get_id()

    @classmethod
    def get_id(cls) -> int:
        cls._current_id += 1
        return cls._current_id
    
    @classmethod
    def write_current_id(cls) -> None:
        with open(cls.FILE_PATH, "w") as file:
            file.write(str(cls._current_id))

    @classmethod
    def reset(cls) -> None:
        cls._current_id = 0

    def to_JSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4
        )
    
    @classmethod
    def get_task_id(cls) -> None:
        try:
            with open(cls.FILE_PATH, "r") as file:
                id = file.read()
                cls._current_id = int(id)
        
        except FileNotFoundError:
            with open(cls.FILE_PATH, "w") as file:
                file.write("0")
                cls._current_id = 0