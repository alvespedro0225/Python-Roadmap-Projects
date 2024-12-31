from datetime import datetime
from pydantic import BaseModel, validate_call

class Utils(BaseModel):

    @staticmethod
    @validate_call
    def get_current_time() -> str:
        return datetime.now().strftime("%d%m%Y, %H%M%S")