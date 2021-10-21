""" Star Wars API client using swapi-python python package

Package used underneath this client:
https://github.com/phalt/swapi-python
"""
from typing import Generator

import requests

from python_star_wars_api_client.domain.aggregates import AggregateSet, CharacterSet, SpeciesSet
from python_star_wars_api_client.domain.interfaces.swapi import StarWarsApiInterface
from python_star_wars_api_client.domain.models import Character, Model, Species


class StarWarsApiWithRequests(StarWarsApiInterface):
    def get_all_characters(self) -> CharacterSet:
        """Fetch SW API to get all the characters (/people endpoint)

        Returns:
            A populated CharacterSet with all the SW API results
        """
        all_characters = CharacterSet([])

        for characters in self._get_resources(CharacterSet, Character, self.PEOPLE):
            all_characters.extend(characters)

        return all_characters

    def get_all_species(self) -> SpeciesSet:
        """Fetch SW API to get all the species (/species endpoint)

        Returns:
            A populated SpeciesSet with all the SW API results
        """
        all_species = SpeciesSet([])

        for species in self._get_resources(SpeciesSet, Species, self.SPECIES):
            all_species.extend(species)

        return all_species

    def _get_resources(
        self, aggregate_class: type[AggregateSet], model_class: type[Model], url_path: str
    ) -> Generator[AggregateSet, None, None]:
        next_page = f"{self.BASE_URL}/{url_path}"
        while next_page:
            response = requests.get(next_page).json()
            characters = aggregate_class([model_class(**result) for result in response["results"]])
            yield characters
            next_page = response["next"]
