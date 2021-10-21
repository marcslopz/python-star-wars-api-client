""" Star Wars API interface class
"""
from python_star_wars_api_client.domain.aggregates import CharacterSet, SpeciesSet


class StarWarsApiInterface:
    BASE_URL = "https://swapi.dev/api"
    PEOPLE = "people"
    SPECIES = "species"
    FILMS = "films"

    def get_all_characters(self) -> CharacterSet:
        """Fetch SW API to get all the characters (/people endpoint)

        Returns:
            A populated CharacterSet with all the SW API results

        # noqa: DAR202
        # noqa: DAR401
        """
        raise NotImplementedError

    def get_all_species(self) -> SpeciesSet:
        """Fetch SW API to get all the species (/species endpoint)

        Returns:
            A populated SpeciesSet with all the SW API results

        # noqa: DAR202
        # noqa: DAR401
        """
        raise NotImplementedError
