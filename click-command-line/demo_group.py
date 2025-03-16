import click


@click.group()
def cli():
    pass

@cli.command(help="This command will initialize the database")
@click.option("--name", help="name of database to init")
@click.option("--server", help="name of server on which db to init resides")
def initdb(server: str,name: str):
    click.echo(f'Initialized the database {server=} , {name=}')

@cli.command(help="This command will drop the database")
@click.option("--name", help="name of database to drop")
@click.option("--server", help="name of server on which db to drop resides")
def dropdb(name:str,server:str):
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()
