"""Tests for swapi_app module."""
from typing import Any

import json
from unittest import TestCase, mock

from python_star_wars_api_client.application.swapi_app import StarWarsApiClientApp
from python_star_wars_api_client.infrastructure.swapi.with_requests import StarWarsApiWithRequests


def read_json_file(path: str) -> dict[str, Any]:
    with open(path) as f:
        content = json.loads(f.read())
    return content


# Characters deserialized JSONs
CHARACTERS_ONLY_ONE_CHARACTER = read_json_file("tests/fixtures/characters/only_one_character.json")
CHARACTERS_ONLY_ONE_PAGE = read_json_file("tests/fixtures/characters/only_one_page.json")
CHARACTERS_PAGE_ONE_OF_TWO = read_json_file("tests/fixtures/characters/page_one_of_two.json")
CHARACTERS_PAGE_TWO_OF_TWO = read_json_file("tests/fixtures/characters/page_two_of_two.json")
UNORDERED_CHARACTERS_BY_FILMS_AND_HEIGHT_AND_NAME = read_json_file("tests/fixtures/characters/unordered.json")

# Species deserialized JSONs
SPECIES_ONLY_ONE_SPECIES = read_json_file("tests/fixtures/species/only_one_species.json")
SPECIES_ONLY_ONE_PAGE = read_json_file("tests/fixtures/species/only_one_page.json")
SPECIES_PAGE_ONE_OF_TWO = read_json_file("tests/fixtures/species/page_one_of_two.json")
SPECIES_PAGE_TWO_OF_TWO = read_json_file("tests/fixtures/species/page_two_of_two.json")
UNORDERED_SPECIES_BY_ID_AND_NAME = read_json_file("tests/fixtures/species/unordered.json")


@mock.patch("python_star_wars_api_client.infrastructure.swapi.with_requests.requests")
class SwapiAppGetCharactersTestCase(TestCase):
    def setUp(self) -> None:
        self.swapi_app = StarWarsApiClientApp(StarWarsApiWithRequests)

    def test_empty_characters_from_swapi_should_return_empty_characterset(self, mock_requests):
        mock_requests.get.return_value.json.return_value = {"count": 0, "next": None, "previous": None, "results": []}
        should_be_zero_characters = self.swapi_app.get_characters()
        self.assertEqual(0, len(should_be_zero_characters))

    def test_one_character_returned_from_swapi_should_return_characterset_with_the_same_character(self, mock_requests):
        mock_requests.get.return_value.json.return_value = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": "Luke Skywalker",
                    "height": "172",
                    "mass": "77",
                    "hair_color": "blond",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "19BBY",
                    "gender": "male",
                    "homeworld": "https://swapi.dev/api/planets/1/",
                    "films": [
                        "https://swapi.dev/api/films/1/",
                        "https://swapi.dev/api/films/2/",
                        "https://swapi.dev/api/films/3/",
                        "https://swapi.dev/api/films/6/",
                    ],
                    "species": [],
                    "vehicles": ["https://swapi.dev/api/vehicles/14/", "https://swapi.dev/api/vehicles/30/"],
                    "starships": ["https://swapi.dev/api/starships/12/", "https://swapi.dev/api/starships/22/"],
                    "created": "2014-12-09T13:50:51.644000Z",
                    "edited": "2014-12-20T21:17:56.891000Z",
                    "url": "https://swapi.dev/api/people/1/",
                },
            ],
        }
        should_be_one_character = self.swapi_app.get_characters()
        self.assertEqual(1, len(should_be_one_character))

    def test_one_page_returned_from_swapi_should_return_characterset_with_the_same_characters(self, mock_requests):
        mock_requests.get.return_value.json.return_value = CHARACTERS_ONLY_ONE_PAGE
        should_be_ten_characters = self.swapi_app.get_characters()
        self.assertEqual(10, len(should_be_ten_characters))

    def test_more_than_one_page_returned_from_swapi_should_return_characterset_with_only_ten_characters(
        self, mock_requests
    ):
        mock_requests.get.return_value.json.side_effect = [
            CHARACTERS_PAGE_ONE_OF_TWO,
            CHARACTERS_PAGE_TWO_OF_TWO,
        ]
        should_be_twenty_character = self.swapi_app.get_characters()
        self.assertEqual(20, len(should_be_twenty_character))

    def test_limit_below_results_should_truncate_characterset(self, mock_requests):
        mock_requests.get.return_value.json.return_value = CHARACTERS_ONLY_ONE_PAGE
        should_be_one_character = self.swapi_app.get_characters(limit=1)
        self.assertEqual(1, len(should_be_one_character))

    def test_limit_above_results_should_return_the_same_characterset(self, mock_requests):
        mock_requests.get.return_value.json.return_value = CHARACTERS_ONLY_ONE_PAGE
        should_be_ten_characters = self.swapi_app.get_characters(limit=11)
        self.assertEqual(10, len(should_be_ten_characters))

    def test_negative_limit_results_should_raise_exception(self, mock_requests):
        mock_requests.get.return_value.json.return_value = CHARACTERS_ONLY_ONE_PAGE
        self.assertRaises(ValueError, lambda: self.swapi_app.get_characters(limit=-1))

    def test_ordering_by_film_amount(self, mock_requests):
        mock_requests.get.return_value.json.return_value = UNORDERED_CHARACTERS_BY_FILMS_AND_HEIGHT_AND_NAME
        should_be_two_characters = self.swapi_app.get_characters(order_by="films")
        self.assertEqual(2, len(should_be_two_characters))
        self.assertEqual("Han Solo", should_be_two_characters[0].name)

    def test_ordering_by_height(self, mock_requests):
        mock_requests.get.return_value.json.return_value = UNORDERED_CHARACTERS_BY_FILMS_AND_HEIGHT_AND_NAME
        should_be_two_characters = self.swapi_app.get_characters(order_by="height")
        self.assertEqual(2, len(should_be_two_characters))
        self.assertEqual("Han Solo", should_be_two_characters[0].name)

    def test_ordering_by_name(self, mock_requests):
        mock_requests.get.return_value.json.return_value = UNORDERED_CHARACTERS_BY_FILMS_AND_HEIGHT_AND_NAME
        should_be_two_characters = self.swapi_app.get_characters(order_by="name")
        self.assertEqual(2, len(should_be_two_characters))
        self.assertEqual("Han Solo", should_be_two_characters[0].name)

    def test_ordering_by_unexisting_attribute(self, mock_requests):
        mock_requests.get.return_value.json.return_value = UNORDERED_CHARACTERS_BY_FILMS_AND_HEIGHT_AND_NAME
        self.assertRaises(ValueError, lambda: self.swapi_app.get_characters(order_by="oops"))


@mock.patch("python_star_wars_api_client.infrastructure.swapi.with_requests.requests")
class SwapiAppGetSpeciesTestCase(TestCase):
    def setUp(self) -> None:
        self.swapi_app = StarWarsApiClientApp(StarWarsApiWithRequests)

    def test_empty_species_from_swapi_should_return_empty_species_set(self, mock_requests):
        mock_requests.get.return_value.json.return_value = {"count": 0, "next": None, "previous": None, "results": []}
        returned_species = self.swapi_app.get_species()
        self.assertEqual(0, len(returned_species))

    def test_one_species_returned_from_swapi_should_return_species_set_with_the_same_species(self, mock_requests):
        mock_requests.get.return_value.json.return_value = SPECIES_ONLY_ONE_SPECIES
        returned_species = self.swapi_app.get_species()
        self.assertEqual(1, len(returned_species))

    def test_one_page_returned_from_swapi_should_return_species_set_with_the_same_species(self, mock_requests):
        mock_requests.get.return_value.json.return_value = SPECIES_ONLY_ONE_PAGE
        returned_species = self.swapi_app.get_species()
        self.assertEqual(10, len(returned_species))

    def test_more_than_one_page_returned_from_swapi_should_return_species_set_with_only_ten_species(
        self, mock_requests
    ):
        mock_requests.get.return_value.json.side_effect = [
            SPECIES_PAGE_ONE_OF_TWO,
            SPECIES_PAGE_TWO_OF_TWO,
        ]
        returned_species = self.swapi_app.get_species()
        self.assertEqual(20, len(returned_species))

    def test_limit_below_results_should_truncate_species_set(self, mock_requests):
        mock_requests.get.return_value.json.return_value = SPECIES_ONLY_ONE_PAGE
        returned_species = self.swapi_app.get_species(limit=1)
        self.assertEqual(1, len(returned_species))

    def test_limit_above_results_should_return_the_same_species_set(self, mock_requests):
        mock_requests.get.return_value.json.return_value = SPECIES_ONLY_ONE_PAGE
        returned_species = self.swapi_app.get_species(limit=11)
        self.assertEqual(10, len(returned_species))

    def test_negative_limit_results_should_raise_exception(self, mock_requests):
        mock_requests.get.return_value.json.return_value = SPECIES_ONLY_ONE_PAGE
        self.assertRaises(ValueError, lambda: self.swapi_app.get_species(limit=-1))

    def test_ordering_by_id(self, mock_requests):
        mock_requests.get.return_value.json.return_value = UNORDERED_SPECIES_BY_ID_AND_NAME
        returned_species = self.swapi_app.get_species(order_by="id")
        self.assertEqual(2, len(returned_species))
        self.assertEqual("Human", returned_species[0].name)

    def test_ordering_by_name(self, mock_requests):
        mock_requests.get.return_value.json.return_value = UNORDERED_SPECIES_BY_ID_AND_NAME
        returned_species = self.swapi_app.get_species(order_by="name")
        self.assertEqual(2, len(returned_species))
        self.assertEqual("Human", returned_species[0].name)

    def test_ordering_by_unexisting_attribute(self, mock_requests):
        mock_requests.get.return_value.json.return_value = UNORDERED_SPECIES_BY_ID_AND_NAME
        self.assertRaises(ValueError, lambda: self.swapi_app.get_species(order_by="oops"))
