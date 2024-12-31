from pydantic import BaseModel, validate_call
from typing import ClassVar, Any

from .Utils import Utils

class Task(BaseModel):


    FILE_PATH:ClassVar[str] = "./Id.txt"
    _current_id:ClassVar[int]
    id:int
    created_at:str = Utils.get_current_time()
    updated_at:str = Utils.get_current_time()
    status:str  
    description:str
    

    def __init__(self) -> None:
        super().__init__(
            _currentid=self.get_current_id(),
            id = self.get_id()
            )

    @classmethod
    @validate_call
    def get_current_id(cls) -> int:
        try:
            with open(cls.FILE_PATH, "r") as file:
                id = file.read()
                return int(id)
        
        except FileNotFoundError:
            with open(cls.FILE_PATH, "w") as file:
                file.write("0")
                return 0

    @classmethod
    @validate_call
    def get_id(cls) -> int:
        cls._current_id += 1
        return cls._current_id
    
    @classmethod
    @validate_call
    def write_current_id(cls):
        with open(cls.FILE_PATH, "w") as file:
            file.write(str(cls._current_id))