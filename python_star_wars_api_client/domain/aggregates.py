from __future__ import annotations

from python_star_wars_api_client.domain.models import Character, Model, Species


def sort_key(character: Character, order_by: str):
    character_attribute = getattr(character, order_by)
    if isinstance(character_attribute, list):
        return len(character_attribute)

    try:
        return int(character_attribute)
    except ValueError:
        return character_attribute


class AggregateSet:
    model_class = Model

    def __init__(self, items: list[model_class]):
        self.items = items

    def sort(self, order_by: str, descending: bool = True) -> None:
        """Sort the current AggregateSet by `order_by` model_class's attribute

        Args:
          order_by: model_class's attribute name to be used as ordering (descending)
          descending: descending order if True, ascending order if False

        Raises:
            ValueError if `order_by` is not a valid model_class's attribute name
        """
        if not self.model_class.is_valid_field(order_by):
            raise ValueError(f"'{order_by}' is not a valid attribute of {self.model_class} class")
        self.items.sort(key=lambda i: sort_key(i, order_by), reverse=descending)

    def limit(self, limit: int) -> None:
        """Truncates the current elements up to `limit` elements

        Args:
          limit: number of items returned (if it's bigger than the size of self.items, all will be returned)

        Raises:
            ValueError if `limit` is negative
        """
        if limit < 0:
            raise ValueError(f"limit with negative value ({limit})")
        self.items = self.items[:limit]

    def extend(self, items_to_extend: AggregateSet):
        self.items.extend(items_to_extend.items)

    def csv(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index: int):
        return self.items[index]

    def __repr__(self):
        return f"<{self.__class__.__name__} [{len(self.items)} {self.model_class.__name__}]>"


class CharacterSet(AggregateSet):
    model_class = Character


class SpeciesSet(AggregateSet):
    model_class = Species
