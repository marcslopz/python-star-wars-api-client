# type: ignore[attr-defined]
from typing import Optional

from enum import Enum

import typer
from rich.console import Console

from python_star_wars_api_client import version
from python_star_wars_api_client.application.swapi_app import StarWarsApiClientApp
from python_star_wars_api_client.domain.aggregates import CharacterSet
from python_star_wars_api_client.infrastructure.httpbin.with_requests import send_csv
from python_star_wars_api_client.infrastructure.swapi.with_requests import StarWarsApiWithRequests


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="python-star-wars-api-client",
    help="Star Wars API Client",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]python-star-wars-api-client[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Person to greet."),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for print. If not specified then choice will be random.",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the python-star-wars-api-client package.",
    ),
) -> None:
    swapi_app = StarWarsApiClientApp(StarWarsApiWithRequests)
    most_appearing_ten_characters: CharacterSet = swapi_app.get_characters("films", 10)
    most_appearing_ten_characters_by_height = most_appearing_ten_characters.get_characters_ordered_by("height")
    csv = most_appearing_ten_characters_by_height.csv()
    send_csv("ten_most_appearing_sw_characters.csv", csv)


if __name__ == "__main__":
    app()
