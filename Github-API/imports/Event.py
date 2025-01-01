from pydantic import BaseModel
from typing import Any


class GithubEvent(BaseModel):

    id: int
    type: str
    actor: dict[str, Any]
    repo: dict[str, Any]
    public: bool
    created_at: str
