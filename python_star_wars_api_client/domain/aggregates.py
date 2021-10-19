from __future__ import annotations

from python_star_wars_api_client.domain.models import Character


def sort_key(character: Character, order_by: str):
    character_attribute = getattr(character, order_by)
    if isinstance(character_attribute, list):
        return len(character_attribute)

    try:
        return int(character_attribute)
    except ValueError:
        return character_attribute


class CharacterSet:
    def __init__(self, characters: list[Character]):
        self.characters = characters

    def sort(self, order_by: str, descending: bool = True) -> None:
        """Sort the current CharacterSet by `order_by` Character's attribute

        Args:
          order_by: Character's attribute name to be used as ordering (descending)
          descending: descending order if True, ascending order if False

        Raises:
            ValueError if `order_by` is not a valid Character's attribute name
        """
        if not Character.is_valid_field(order_by):
            raise ValueError(f"'{order_by}' is not a valid attribute of Character class")
        self.characters.sort(key=lambda i: sort_key(i, order_by), reverse=descending)

    def limit(self, limit: int) -> None:
        """Truncates the current elements up to `limit` elements

        Args:
          limit: number of characters returned (if it's bigger than the size of characters, all will be returned)

        Raises:
            ValueError if `limit` is negative
        """
        if limit < 0:
            raise ValueError(f"limit with negative value ({limit})")
        self.characters = self.characters[:limit]

    def extend(self, characters_to_extend: CharacterSet):
        self.characters.extend(characters_to_extend.characters)

    def csv(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.characters)

    def __getitem__(self, index: int):
        return self.characters[index]
