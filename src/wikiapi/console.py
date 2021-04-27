import textwrap

import click
import requests

from wikiapi import __version__

WIKIAPI_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The Wikiapi Project."""
    with requests.get(WIKIAPI_URL) as response:
        response.raise_for_status()
        data = response.json()

    click.secho(data["title"], fg="blue")
    click.echo(textwrap.fill(data["extract"]))
