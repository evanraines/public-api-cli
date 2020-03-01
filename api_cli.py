import click
import requests
from random import choice

BASE_URL = "https://api.publicapis.org"
@click.group()
def apis():
    """A CLI Wrapper for the API of Public Apis"""


@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-t', '--title', help="Name of API (matches via substring - i.e. 'at' would return 'cat' and 'atlas')")
@click.option('-c', '--category', help="Return only APIs from this category")
@apis.command()
def entries(no_auth: bool, title: str, category: str):
    """List all cataloged APIs"""

    params = {
        'title': title,
        'category': category
    }
    
    if no_auth:
        params['auth'] = 'null'

    response = requests.get(url=f"{BASE_URL}/entries", params=params)
    if response.status_code == 200:
        for i, entry in enumerate(response.json()['entries']):
            pretty_entry = '\n'.join(f'{k}: {v}' for k, v in entry.items())
            print(f'{i+1}.\n{pretty_entry}\n')
    else:
        print(f'Could not get the categories: {response.text}')

@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-t', '--title', help="Name of API (matches via substring - i.e. 'at' would return 'cat' and 'atlas')")
@click.option('-c', '--category', help="Return only APIs from this category")
@apis.command()
def random(no_auth: bool, title: str, category: str):
    """Get a random API"""

    params = {
        'title': title,
        'category': category
    }
    
    if no_auth:
        params['auth'] = 'null'

    response = requests.get(url=f"{BASE_URL}/entries", params=params)
    if response.status_code == 200:

        pretty_entry = '\n'.join(
            f'{k}: {v}' for k, v in choice(response.json()['entries']).items()
        )

        print(pretty_entry)

    else:
        print(f'Could not get the categories: {response.text}')

@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-t', '--title', help="Name of API (matches via substring - i.e. 'at' would return 'cat' and 'atlas')")
@click.option('-c', '--category', help="Return only APIs from this category")
@apis.command()
def categories(no_auth: bool, title: str, category: str):
    """List all categories"""
    response = requests.get(url=f"{BASE_URL}/categories")
    if response.status_code == 200:
        print('\n'.join(response.json()))
    else:
        print(f'Could not get the categories: {response.text}')

if __name__ == "__main__":
    apis(prog_name="apis")
