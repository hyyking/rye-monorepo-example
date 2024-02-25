import click
import firstpackage as fp


@click.command()
def hello() -> str:
    return click.echo(fp.hello())
