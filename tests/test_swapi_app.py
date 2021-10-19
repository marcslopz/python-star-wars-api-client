"""Tests for swapi_app module."""
import json
from unittest import TestCase, mock

from python_star_wars_api_client.application.swapi_app import StarWarsApiClientApp
from python_star_wars_api_client.infrastructure.swapi.with_requests import StarWarsApiWithRequests

PAGE_ONE_JSON_WITHOUT_NEXT = """
{
    "count": 82,
    "next": null,
    "previous": null,
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
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/14/",
                "https://swapi.dev/api/vehicles/30/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/12/",
                "https://swapi.dev/api/starships/22/"
            ],
            "created": "2014-12-09T13:50:51.644000Z",
            "edited": "2014-12-20T21:17:56.891000Z",
            "url": "https://swapi.dev/api/people/1/"
        },
        {
            "name": "C-3PO",
            "height": "167",
            "mass": "75",
            "hair_color": "n/a",
            "skin_color": "gold",
            "eye_color": "yellow",
            "birth_year": "112BBY",
            "gender": "n/a",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [
                "https://swapi.dev/api/species/2/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:10:51.357000Z",
            "edited": "2014-12-20T21:17:50.309000Z",
            "url": "https://swapi.dev/api/people/2/"
        },
        {
            "name": "R2-D2",
            "height": "96",
            "mass": "32",
            "hair_color": "n/a",
            "skin_color": "white, blue",
            "eye_color": "red",
            "birth_year": "33BBY",
            "gender": "n/a",
            "homeworld": "https://swapi.dev/api/planets/8/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [
                "https://swapi.dev/api/species/2/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:11:50.376000Z",
            "edited": "2014-12-20T21:17:50.311000Z",
            "url": "https://swapi.dev/api/people/3/"
        },
        {
            "name": "Darth Vader",
            "height": "202",
            "mass": "136",
            "hair_color": "none",
            "skin_color": "white",
            "eye_color": "yellow",
            "birth_year": "41.9BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [
                "https://swapi.dev/api/starships/13/"
            ],
            "created": "2014-12-10T15:18:20.704000Z",
            "edited": "2014-12-20T21:17:50.313000Z",
            "url": "https://swapi.dev/api/people/4/"
        },
        {
            "name": "Leia Organa",
            "height": "150",
            "mass": "49",
            "hair_color": "brown",
            "skin_color": "light",
            "eye_color": "brown",
            "birth_year": "19BBY",
            "gender": "female",
            "homeworld": "https://swapi.dev/api/planets/2/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/30/"
            ],
            "starships": [],
            "created": "2014-12-10T15:20:09.791000Z",
            "edited": "2014-12-20T21:17:50.315000Z",
            "url": "https://swapi.dev/api/people/5/"
        },
        {
            "name": "Owen Lars",
            "height": "178",
            "mass": "120",
            "hair_color": "brown, grey",
            "skin_color": "light",
            "eye_color": "blue",
            "birth_year": "52BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:52:14.024000Z",
            "edited": "2014-12-20T21:17:50.317000Z",
            "url": "https://swapi.dev/api/people/6/"
        },
        {
            "name": "Beru Whitesun lars",
            "height": "165",
            "mass": "75",
            "hair_color": "brown",
            "skin_color": "light",
            "eye_color": "blue",
            "birth_year": "47BBY",
            "gender": "female",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:53:41.121000Z",
            "edited": "2014-12-20T21:17:50.319000Z",
            "url": "https://swapi.dev/api/people/7/"
        },
        {
            "name": "R5-D4",
            "height": "97",
            "mass": "32",
            "hair_color": "n/a",
            "skin_color": "white, red",
            "eye_color": "red",
            "birth_year": "unknown",
            "gender": "n/a",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/"
            ],
            "species": [
                "https://swapi.dev/api/species/2/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:57:50.959000Z",
            "edited": "2014-12-20T21:17:50.321000Z",
            "url": "https://swapi.dev/api/people/8/"
        },
        {
            "name": "Biggs Darklighter",
            "height": "183",
            "mass": "84",
            "hair_color": "black",
            "skin_color": "light",
            "eye_color": "brown",
            "birth_year": "24BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [
                "https://swapi.dev/api/starships/12/"
            ],
            "created": "2014-12-10T15:59:50.509000Z",
            "edited": "2014-12-20T21:17:50.323000Z",
            "url": "https://swapi.dev/api/people/9/"
        },
        {
            "name": "Obi-Wan Kenobi",
            "height": "182",
            "mass": "77",
            "hair_color": "auburn, white",
            "skin_color": "fair",
            "eye_color": "blue-gray",
            "birth_year": "57BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/20/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/38/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/48/",
                "https://swapi.dev/api/starships/59/",
                "https://swapi.dev/api/starships/64/",
                "https://swapi.dev/api/starships/65/",
                "https://swapi.dev/api/starships/74/"
            ],
            "created": "2014-12-10T16:16:29.192000Z",
            "edited": "2014-12-20T21:17:50.325000Z",
            "url": "https://swapi.dev/api/people/10/"
        }
    ]
}
"""

PAGE_ONE_JSON_WITH_NEXT = """
{
    "count": 82,
    "next": "https://swapi.dev/api/people/?page=2",
    "previous": null,
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
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/14/",
                "https://swapi.dev/api/vehicles/30/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/12/",
                "https://swapi.dev/api/starships/22/"
            ],
            "created": "2014-12-09T13:50:51.644000Z",
            "edited": "2014-12-20T21:17:56.891000Z",
            "url": "https://swapi.dev/api/people/1/"
        },
        {
            "name": "C-3PO",
            "height": "167",
            "mass": "75",
            "hair_color": "n/a",
            "skin_color": "gold",
            "eye_color": "yellow",
            "birth_year": "112BBY",
            "gender": "n/a",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [
                "https://swapi.dev/api/species/2/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:10:51.357000Z",
            "edited": "2014-12-20T21:17:50.309000Z",
            "url": "https://swapi.dev/api/people/2/"
        },
        {
            "name": "R2-D2",
            "height": "96",
            "mass": "32",
            "hair_color": "n/a",
            "skin_color": "white, blue",
            "eye_color": "red",
            "birth_year": "33BBY",
            "gender": "n/a",
            "homeworld": "https://swapi.dev/api/planets/8/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [
                "https://swapi.dev/api/species/2/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:11:50.376000Z",
            "edited": "2014-12-20T21:17:50.311000Z",
            "url": "https://swapi.dev/api/people/3/"
        },
        {
            "name": "Darth Vader",
            "height": "202",
            "mass": "136",
            "hair_color": "none",
            "skin_color": "white",
            "eye_color": "yellow",
            "birth_year": "41.9BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [
                "https://swapi.dev/api/starships/13/"
            ],
            "created": "2014-12-10T15:18:20.704000Z",
            "edited": "2014-12-20T21:17:50.313000Z",
            "url": "https://swapi.dev/api/people/4/"
        },
        {
            "name": "Leia Organa",
            "height": "150",
            "mass": "49",
            "hair_color": "brown",
            "skin_color": "light",
            "eye_color": "brown",
            "birth_year": "19BBY",
            "gender": "female",
            "homeworld": "https://swapi.dev/api/planets/2/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/30/"
            ],
            "starships": [],
            "created": "2014-12-10T15:20:09.791000Z",
            "edited": "2014-12-20T21:17:50.315000Z",
            "url": "https://swapi.dev/api/people/5/"
        },
        {
            "name": "Owen Lars",
            "height": "178",
            "mass": "120",
            "hair_color": "brown, grey",
            "skin_color": "light",
            "eye_color": "blue",
            "birth_year": "52BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:52:14.024000Z",
            "edited": "2014-12-20T21:17:50.317000Z",
            "url": "https://swapi.dev/api/people/6/"
        },
        {
            "name": "Beru Whitesun lars",
            "height": "165",
            "mass": "75",
            "hair_color": "brown",
            "skin_color": "light",
            "eye_color": "blue",
            "birth_year": "47BBY",
            "gender": "female",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:53:41.121000Z",
            "edited": "2014-12-20T21:17:50.319000Z",
            "url": "https://swapi.dev/api/people/7/"
        },
        {
            "name": "R5-D4",
            "height": "97",
            "mass": "32",
            "hair_color": "n/a",
            "skin_color": "white, red",
            "eye_color": "red",
            "birth_year": "unknown",
            "gender": "n/a",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/"
            ],
            "species": [
                "https://swapi.dev/api/species/2/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T15:57:50.959000Z",
            "edited": "2014-12-20T21:17:50.321000Z",
            "url": "https://swapi.dev/api/people/8/"
        },
        {
            "name": "Biggs Darklighter",
            "height": "183",
            "mass": "84",
            "hair_color": "black",
            "skin_color": "light",
            "eye_color": "brown",
            "birth_year": "24BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/1/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [
                "https://swapi.dev/api/starships/12/"
            ],
            "created": "2014-12-10T15:59:50.509000Z",
            "edited": "2014-12-20T21:17:50.323000Z",
            "url": "https://swapi.dev/api/people/9/"
        },
        {
            "name": "Obi-Wan Kenobi",
            "height": "182",
            "mass": "77",
            "hair_color": "auburn, white",
            "skin_color": "fair",
            "eye_color": "blue-gray",
            "birth_year": "57BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/20/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/38/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/48/",
                "https://swapi.dev/api/starships/59/",
                "https://swapi.dev/api/starships/64/",
                "https://swapi.dev/api/starships/65/",
                "https://swapi.dev/api/starships/74/"
            ],
            "created": "2014-12-10T16:16:29.192000Z",
            "edited": "2014-12-20T21:17:50.325000Z",
            "url": "https://swapi.dev/api/people/10/"
        }
    ]
}
"""

PAGE_TWO_JSON_WITHOUT_NEXT = """
{
    "count": 82,
    "next": null,
    "previous": "https://swapi.dev/api/people/?page=1",
    "results": [
        {
            "name": "Anakin Skywalker",
            "height": "188",
            "mass": "84",
            "hair_color": "blond",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "41.9BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/1/",
            "films": [
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/44/",
                "https://swapi.dev/api/vehicles/46/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/39/",
                "https://swapi.dev/api/starships/59/",
                "https://swapi.dev/api/starships/65/"
            ],
            "created": "2014-12-10T16:20:44.310000Z",
            "edited": "2014-12-20T21:17:50.327000Z",
            "url": "https://swapi.dev/api/people/11/"
        },
        {
            "name": "Wilhuff Tarkin",
            "height": "180",
            "mass": "unknown",
            "hair_color": "auburn, grey",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "64BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/21/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T16:26:56.138000Z",
            "edited": "2014-12-20T21:17:50.330000Z",
            "url": "https://swapi.dev/api/people/12/"
        },
        {
            "name": "Chewbacca",
            "height": "228",
            "mass": "112",
            "hair_color": "brown",
            "skin_color": "unknown",
            "eye_color": "blue",
            "birth_year": "200BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/14/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [
                "https://swapi.dev/api/species/3/"
            ],
            "vehicles": [
                "https://swapi.dev/api/vehicles/19/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/10/",
                "https://swapi.dev/api/starships/22/"
            ],
            "created": "2014-12-10T16:42:45.066000Z",
            "edited": "2014-12-20T21:17:50.332000Z",
            "url": "https://swapi.dev/api/people/13/"
        },
        {
            "name": "Han Solo",
            "height": "180",
            "mass": "80",
            "hair_color": "brown",
            "skin_color": "fair",
            "eye_color": "brown",
            "birth_year": "29BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/22/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [
                "https://swapi.dev/api/starships/10/",
                "https://swapi.dev/api/starships/22/"
            ],
            "created": "2014-12-10T16:49:14.582000Z",
            "edited": "2014-12-20T21:17:50.334000Z",
            "url": "https://swapi.dev/api/people/14/"
        },
        {
            "name": "Greedo",
            "height": "173",
            "mass": "74",
            "hair_color": "n/a",
            "skin_color": "green",
            "eye_color": "black",
            "birth_year": "44BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/23/",
            "films": [
                "https://swapi.dev/api/films/1/"
            ],
            "species": [
                "https://swapi.dev/api/species/4/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T17:03:30.334000Z",
            "edited": "2014-12-20T21:17:50.336000Z",
            "url": "https://swapi.dev/api/people/15/"
        },
        {
            "name": "Jabba Desilijic Tiure",
            "height": "175",
            "mass": "1,358",
            "hair_color": "n/a",
            "skin_color": "green-tan, brown",
            "eye_color": "orange",
            "birth_year": "600BBY",
            "gender": "hermaphrodite",
            "homeworld": "https://swapi.dev/api/planets/24/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/"
            ],
            "species": [
                "https://swapi.dev/api/species/5/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T17:11:31.638000Z",
            "edited": "2014-12-20T21:17:50.338000Z",
            "url": "https://swapi.dev/api/people/16/"
        },
        {
            "name": "Wedge Antilles",
            "height": "170",
            "mass": "77",
            "hair_color": "brown",
            "skin_color": "fair",
            "eye_color": "hazel",
            "birth_year": "21BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/22/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/"
            ],
            "species": [],
            "vehicles": [
                "https://swapi.dev/api/vehicles/14/"
            ],
            "starships": [
                "https://swapi.dev/api/starships/12/"
            ],
            "created": "2014-12-12T11:08:06.469000Z",
            "edited": "2014-12-20T21:17:50.341000Z",
            "url": "https://swapi.dev/api/people/18/"
        },
        {
            "name": "Jek Tono Porkins",
            "height": "180",
            "mass": "110",
            "hair_color": "brown",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "unknown",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/26/",
            "films": [
                "https://swapi.dev/api/films/1/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [
                "https://swapi.dev/api/starships/12/"
            ],
            "created": "2014-12-12T11:16:56.569000Z",
            "edited": "2014-12-20T21:17:50.343000Z",
            "url": "https://swapi.dev/api/people/19/"
        },
        {
            "name": "Yoda",
            "height": "66",
            "mass": "17",
            "hair_color": "white",
            "skin_color": "green",
            "eye_color": "brown",
            "birth_year": "896BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/28/",
            "films": [
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [
                "https://swapi.dev/api/species/6/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-15T12:26:01.042000Z",
            "edited": "2014-12-20T21:17:50.345000Z",
            "url": "https://swapi.dev/api/people/20/"
        },
        {
            "name": "Palpatine",
            "height": "170",
            "mass": "75",
            "hair_color": "grey",
            "skin_color": "pale",
            "eye_color": "yellow",
            "birth_year": "82BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/8/",
            "films": [
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-15T12:48:05.971000Z",
            "edited": "2014-12-20T21:17:50.347000Z",
            "url": "https://swapi.dev/api/people/21/"
        }
    ]
}
"""

UNORDERED_BY_FILMS_AND_HEIGHT_AND_NAME = """
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Greedo",
            "height": "66",
            "mass": "74",
            "hair_color": "n/a",
            "skin_color": "green",
            "eye_color": "black",
            "birth_year": "44BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/23/",
            "films": [
                "https://swapi.dev/api/films/1/"
            ],
            "species": [
                "https://swapi.dev/api/species/4/"
            ],
            "vehicles": [],
            "starships": [],
            "created": "2014-12-10T17:03:30.334000Z",
            "edited": "2014-12-20T21:17:50.336000Z",
            "url": "https://swapi.dev/api/people/15/"
        },
        {
            "name": "Han Solo",
            "height": "180",
            "mass": "80",
            "hair_color": "brown",
            "skin_color": "fair",
            "eye_color": "brown",
            "birth_year": "29BBY",
            "gender": "male",
            "homeworld": "https://swapi.dev/api/planets/22/",
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/"
            ],
            "species": [],
            "vehicles": [],
            "starships": [
                "https://swapi.dev/api/starships/10/",
                "https://swapi.dev/api/starships/22/"
            ],
            "created": "2014-12-10T16:49:14.582000Z",
            "edited": "2014-12-20T21:17:50.334000Z",
            "url": "https://swapi.dev/api/people/14/"
        }
        ]
}
"""


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
        mock_requests.get.return_value.json.return_value = json.loads(PAGE_ONE_JSON_WITHOUT_NEXT)
        should_be_ten_characters = self.swapi_app.get_characters()
        self.assertEqual(10, len(should_be_ten_characters))

    def test_more_than_one_page_returned_from_swapi_should_return_characterset_with_only_ten_ordered_characters(
        self, mock_requests
    ):
        mock_requests.get.return_value.json.side_effect = [
            json.loads(PAGE_ONE_JSON_WITH_NEXT),
            json.loads(PAGE_TWO_JSON_WITHOUT_NEXT),
        ]
        should_be_twenty_character = self.swapi_app.get_characters()
        self.assertEqual(20, len(should_be_twenty_character))

    def test_limit_below_results_should_truncate_characterset(self, mock_requests):
        mock_requests.get.return_value.json.return_value = json.loads(PAGE_ONE_JSON_WITHOUT_NEXT)
        should_be_one_character = self.swapi_app.get_characters(limit=1)
        self.assertEqual(1, len(should_be_one_character))

    def test_limit_above_results_should_return_the_same_characterset(self, mock_requests):
        mock_requests.get.return_value.json.return_value = json.loads(PAGE_ONE_JSON_WITHOUT_NEXT)
        should_be_ten_characters = self.swapi_app.get_characters(limit=11)
        self.assertEqual(10, len(should_be_ten_characters))

    def test_negative_limit_results_should_raise_exception(self, mock_requests):
        mock_requests.get.return_value.json.return_value = json.loads(PAGE_ONE_JSON_WITHOUT_NEXT)
        self.assertRaises(ValueError, lambda: self.swapi_app.get_characters(limit=-1))

    def test_ordering_by_film_amount(self, mock_requests):
        mock_requests.get.return_value.json.return_value = json.loads(UNORDERED_BY_FILMS_AND_HEIGHT_AND_NAME)
        should_be_two_characters = self.swapi_app.get_characters(order_by="films")
        self.assertEqual(2, len(should_be_two_characters))
        self.assertEqual("Han Solo", should_be_two_characters[0].name)

    def test_ordering_by_height(self, mock_requests):
        mock_requests.get.return_value.json.return_value = json.loads(UNORDERED_BY_FILMS_AND_HEIGHT_AND_NAME)
        should_be_two_characters = self.swapi_app.get_characters(order_by="height")
        self.assertEqual(2, len(should_be_two_characters))
        self.assertEqual("Han Solo", should_be_two_characters[0].name)

    def test_ordering_by_name(self, mock_requests):
        mock_requests.get.return_value.json.return_value = json.loads(UNORDERED_BY_FILMS_AND_HEIGHT_AND_NAME)
        should_be_two_characters = self.swapi_app.get_characters(order_by="name")
        self.assertEqual(2, len(should_be_two_characters))
        self.assertEqual("Han Solo", should_be_two_characters[0].name)

    def test_ordering_by_unexisting_attribute(self, mock_requests):
        mock_requests.get.return_value.json.return_value = json.loads(UNORDERED_BY_FILMS_AND_HEIGHT_AND_NAME)
        self.assertRaises(ValueError, lambda: self.swapi_app.get_characters(order_by="oops"))
