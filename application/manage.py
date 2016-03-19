# -*- encoding: utf-8 ---------------------------------------------------------


import click
from serve import db


@click.group()
def cli():
    pass


@cli.command()
def create():
    db.create_all()
    print('Database created')


@cli.command()
def remove():
    print('removed')


@cli.command()
def clear():
    db.drop_all()
    print('Database cleared')


if __name__ == '__main__':
    cli()
