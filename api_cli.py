import click

@click.group()
def apis():
    """A CLI Wrapper for the API of Public Apis"""


@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-t', '--title', help="Name of API (matches via substring - i.e. 'at' would return 'cat' and 'atlas')")
@click.option('-c', '--category', help="Return only APIs from this category")
@apis.command()
def entries(no_auth: bool, title: str, category: str):
    """List all cataloged APIs"""

@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-t', '--title', help="Name of API (matches via substring - i.e. 'at' would return 'cat' and 'atlas')")
@click.option('-c', '--category', help="Return only APIs from this category")
@apis.command()
def random(no_auth: bool, title: str, category: str):
    """Get a random API"""

@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@click.option('-t', '--title', help="Name of API (matches via substring - i.e. 'at' would return 'cat' and 'atlas')")
@click.option('-c', '--category', help="Return only APIs from this category")
@apis.command()
def categories(no_auth: bool, title: str, category: str):
    """List all categories"""

if __name__ == "__main__":
    apis(prog_name="apis")
