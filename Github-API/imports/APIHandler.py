from requests import ConnectionError
from requests import get as http_get
from pydantic import BaseModel, validate_call
from typing import ClassVar
from pprint import pprint

from .Event import GithubEvent


class APIHandler(BaseModel):

    BASE_URI: ClassVar[str] = "https://api.github.com"

    @classmethod
    @validate_call
    def get_info(cls, username: str) -> None:
        try:
            response = http_get(f"{cls.BASE_URI}/users/{username}/events")
            response = response.json()
            for event_json in response:
                event = GithubEvent(
                    id=event_json["id"],
                    type=event_json["type"],
                    actor=event_json["actor"],
                    repo=event_json["repo"],
                    public=event_json["public"],
                    created_at=event_json["created_at"],
                )

                pprint(event)
                print()

        except ConnectionError:

            print("Could not connect to the server.")
