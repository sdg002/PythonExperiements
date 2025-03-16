import click

@click.command()
def hello():
    click.echo('Hello World!')

@click.command()
@click.option("-x1")
@click.option("-x2")
def hello2(x1:int, x2:int):
    click.echo('Hello World! 2')

if __name__ == '__main__':
    hello()
