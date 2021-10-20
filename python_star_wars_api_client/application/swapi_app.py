""" Star Wars API client App class

This class will contain all our use cases which consumes from SW API
"""
from typing import Optional

from python_star_wars_api_client.domain.aggregates import CharacterSet, SpeciesSet


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

    def get_species(self, order_by: Optional[str] = None, limit: Optional[int] = None) -> SpeciesSet:
        """Fetches SW Api and gets a limited and/or ordered SpeciesSet

        Args:
          order_by: SpeciesSet's attribute to order the result (descending order), if None, no ordering applied
          limit: number of SpeciesSet to be returned

        Returns:
          A SpeciesSet ordered and limited (if asked to)
        """
        all_species: SpeciesSet = self.swapi_class.get_all_species()
        if order_by:
            all_species.sort(order_by)
        if limit:
            all_species.limit(limit)
        return all_species
