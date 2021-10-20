""" CSVWriter will create csv of our domain models

"""
from python_star_wars_api_client.domain.aggregates import CharacterSet, SpeciesSet


class CSVWriter:
    """CSV Writer application service"""

    CHARACTERS_HEADER = "name,species,height,appearances"

    def get_characters_csv(self, characters: CharacterSet, species: SpeciesSet) -> str:
        """Writes each character row in CSV format

        Example:
            name,species,height,appearances
            Chewbacca,Wookie,228,4

        Args:
          characters: characters to be written on each row
          species: species set which will be used to get species name (since Character model has id as "FK")

        Returns:
          a string CSV-formatted with a row per each input character
        """
        csv_result = self.CHARACTERS_HEADER
        if not characters:
            # avoid sorting species if there is no characters in the input CharacterSet
            return csv_result

        species.sort("id", descending=False)
        for character in characters:
            related_species_name = (species[character.species_ids[0] - 1]).name if character.species_ids else ""
            csv_result += f"\n{character.name},{related_species_name},{character.height},{len(character.films)}"

        return csv_result
