""" Star Wars API client using swapi-python python package

Package used underneath this client:
https://github.com/phalt/swapi-python
"""
import requests

from python_star_wars_api_client.domain.aggregates import CharacterSet
from python_star_wars_api_client.domain.interfaces.swapi import StarWarsApiInterface
from python_star_wars_api_client.domain.models import Character


class StarWarsApiWithRequests(StarWarsApiInterface):
    def get_all_characters(self) -> CharacterSet:
        """Fetch SW API to get all the characters (/people endpoint)

        Returns:
            A populated CharacterSet with all the SW API results
        """
        all_characters = CharacterSet([])

        for characters in self._get_characters():
            all_characters.extend(characters)

        return all_characters

    def _get_characters(self):
        next_page = f"{self.BASE_URL}/{self.PEOPLE}"
        while next_page:
            response = requests.get(next_page).json()
            characters = CharacterSet([Character(**result) for result in response["results"]])
            yield characters
            next_page = response["next"]
