""" Star Wars API client App class

This class will contain all our use cases
"""
from typing import Optional

from python_star_wars_api_client.domain.aggregates import CharacterSet


class StarWarsApiClientApp:
    """Star Wars API client App class"""

    def __init__(self, swapi_class):
        self.swapi_class = swapi_class()

    def get_characters(self, order_by: Optional[str] = None, limit: Optional[int] = None) -> CharacterSet:
        """Fetches SW Api and gets a limited and/or ordered CharacterSet

        Args:
          order_by: Character's attribute to order the result (descending order), if None, no ordering applied
          limit: number of Characters to be returned

        Returns:
          A CharacterSet ordered and limited (if asked to)
        """
        all_characters: CharacterSet = self.swapi_class.get_all_characters()
        if order_by:
            all_characters.sort(order_by)
        if limit:
            all_characters.limit(limit)
        return all_characters
