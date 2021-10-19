""" Star Wars API interface class
"""
from python_star_wars_api_client.domain.aggregates import CharacterSet


class StarWarsApiInterface:
    BASE_URL = "https://swapi.dev/api"
    PEOPLE = "people"

    def get_all_characters(self) -> CharacterSet:
        """Fetch SW API to get all the characters (/people endpoint)

        Returns:
            A populated CharacterSet with all the SW API results
        """
        raise NotImplementedError
