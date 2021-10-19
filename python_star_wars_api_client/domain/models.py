from typing import List

from pydantic import BaseModel


class Character(BaseModel):
    name: str
    height: str  # changed from int to str because some People have "unknown" as height in SW API
    species: list[str]
    films: list[str]

    @classmethod
    def is_valid_field(cls, field):
        return field in cls.__fields__


class Species(BaseModel):
    name: str
