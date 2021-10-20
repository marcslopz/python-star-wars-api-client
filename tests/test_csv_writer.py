"""Tests for swapi_app module."""
from unittest import TestCase

from python_star_wars_api_client.application.csv_writer import CSVWriter
from python_star_wars_api_client.domain.aggregates import CharacterSet, SpeciesSet
from python_star_wars_api_client.domain.interfaces.swapi import StarWarsApiInterface
from python_star_wars_api_client.domain.models import Character, Species


class CsvWriterTestCase(TestCase):
    def setUp(self) -> None:
        self.csv_writer = CSVWriter()
        self.films_url_array = [
            f"{StarWarsApiInterface.BASE_URL}/{StarWarsApiInterface.FILMS}/{i}/" for i in range(1, 5)
        ]
        self.people_base_url = f"{StarWarsApiInterface.BASE_URL}/{StarWarsApiInterface.PEOPLE}"
        self.species_base_url = f"{StarWarsApiInterface.BASE_URL}/{StarWarsApiInterface.SPECIES}"

    def test_write_csv_with_zero_characters_and_zero_species(self):
        csv = self.csv_writer.get_characters_csv(CharacterSet([]), SpeciesSet([]))
        self.assertEqual(CSVWriter.CHARACTERS_HEADER, csv)

    def test_write_csv_with_zero_characters_and_one_species(self):
        one_species = Species(name="Human", url=f"{self.species_base_url}/1/")
        species_set = SpeciesSet([one_species])
        csv = self.csv_writer.get_characters_csv(CharacterSet([]), species_set)
        self.assertEqual(CSVWriter.CHARACTERS_HEADER, csv)

    def test_write_csv_with_one_character_with_no_related_species(self):
        one_character = Character(
            name="Luke Skywalker",
            height="172",
            species=[],
            films=self.films_url_array,
            url=f"{self.people_base_url}/1/",
        )
        character_set = CharacterSet([one_character])

        csv = self.csv_writer.get_characters_csv(character_set, SpeciesSet([]))

        expected_csv = (
            f"{CSVWriter.CHARACTERS_HEADER}\n{one_character.name},,{one_character.height},{len(one_character.films)}"
        )
        self.assertEqual(expected_csv, csv)

    def test_write_csv_with_one_character_with_one_related_species(self):
        one_character = Character(
            name="Chewbacca",
            height="228",
            species=[f"{self.species_base_url}/2/"],
            films=self.films_url_array,
            url=f"{self.people_base_url}/1/",
        )
        character_set = CharacterSet([one_character])

        species_1 = Species(name="Human", url=f"{self.species_base_url}/1/")
        species_2 = Species(name="Wookie", url=f"{self.species_base_url}/2/")
        species_set = SpeciesSet([species_1, species_2])
        csv = self.csv_writer.get_characters_csv(character_set, species_set)

        expected_csv = f"{CSVWriter.CHARACTERS_HEADER}\n{one_character.name},{species_2.name},{one_character.height},{len(one_character.films)}"
        self.assertEqual(expected_csv, csv)

    def test_write_csv_with_more_than_one_character(self):
        character_1 = Character(
            name="Luke Skywalker",
            height="172",
            species=[],
            films=self.films_url_array,
            url=f"{self.people_base_url}/1/",
        )
        character_2 = Character(
            name="Chewbacca",
            height="228",
            species=[f"{self.species_base_url}/2/"],
            films=self.films_url_array,
            url=f"{self.people_base_url}/2/",
        )
        character_set = CharacterSet([character_1, character_2])

        species_1 = Species(name="Human", url=f"{self.species_base_url}/1/")
        species_2 = Species(name="Wookie", url=f"{self.species_base_url}/2/")
        species_set = SpeciesSet([species_1, species_2])
        csv = self.csv_writer.get_characters_csv(character_set, species_set)

        expected_csv = f"{CSVWriter.CHARACTERS_HEADER}\n{character_1.name},,{character_1.height},{len(character_1.films)}\n{character_2.name},{species_2.name},{character_2.height},{len(character_2.films)}"
        self.assertEqual(expected_csv, csv)
