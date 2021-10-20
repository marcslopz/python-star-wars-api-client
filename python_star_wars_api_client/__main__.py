# type: ignore[attr-defined]
import typer
from rich.console import Console

from python_star_wars_api_client import version
from python_star_wars_api_client.application.csv_writer import CSVWriter
from python_star_wars_api_client.application.httpbin_sender import HttpBinSender
from python_star_wars_api_client.application.swapi_app import StarWarsApiClientApp
from python_star_wars_api_client.domain.aggregates import CharacterSet
from python_star_wars_api_client.infrastructure.httpbin.with_requests import HttpBinWithRequests
from python_star_wars_api_client.infrastructure.swapi.with_requests import StarWarsApiWithRequests

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


@app.command()
def main(
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
    most_appearing_ten_characters_by_height: CharacterSet = swapi_app.get_characters("films", 10)
    most_appearing_ten_characters_by_height.sort("height")
    console.print(
        f"[yellow]python-star-wars-api-client[/] returned characters: [bold blue]"
        f"{most_appearing_ten_characters_by_height}[/]"
    )
    all_species = swapi_app.get_species(order_by="id")
    console.print(f"[yellow]python-star-wars-api-client[/] returned species: [bold blue]" f"{all_species}[/]")
    csv_writer = CSVWriter()
    csv: str = csv_writer.get_characters_csv(most_appearing_ten_characters_by_height, all_species)
    console.print(f"[yellow]python-star-wars-api-client[/] csv: \n[bold blue]{csv}[/]")
    httpbin_sender = HttpBinSender(HttpBinWithRequests)
    status_code = httpbin_sender.send_file("swapi_most_appearing_characters.csv", csv)
    console.print(
        f"[yellow]python-star-wars-api-client[/] csv sent to httpbin.org: [bold blue] Response Status {status_code}[/]"
    )


if __name__ == "__main__":
    app()
