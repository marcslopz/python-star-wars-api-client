import re

from pydantic import AnyHttpUrl, BaseModel, validator


def get_id_from_url(url: str) -> int:
    match = re.search(r"(\d+)", url)
    if not match:
        raise ValueError(f"no ID found in url {url}")
    return int(match.group(1))


class Model(BaseModel):
    url: AnyHttpUrl
    id: int = 0

    @validator("id", always=True)
    def id_from_url(cls, v, values, **kwargs):
        return get_id_from_url(values["url"])

    @classmethod
    def is_valid_field(cls, field):
        return field in cls.__fields__


class Character(Model):
    name: str
    height: str  # changed from int to str because some People have "unknown" as height in SW API
    species: list[AnyHttpUrl]
    species_ids: list[int] = []
    films: list[AnyHttpUrl]

    @validator("species_ids", always=True)
    def id_from_url(cls, v, values, **kwargs):
        return [get_id_from_url(species_url) for species_url in values["species"]]


class Species(Model):
    name: str


class ModelID(BaseModel):
    id: int
