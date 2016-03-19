# -*- encoding: utf-8 ---------------------------------------------------------


import click
import csv

from serve import db
from models import *


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


@cli.command()
@click.option('--name', type=str, required=True)
@click.option('--directory', type=click.Path(exists=True), required=True)
def add_dataset(name, directory):
    dataset = Dataset(name)
    db.session.add(dataset)
    db.session.commit()
    print('Dataset #{} added'.format(dataset.id))


@cli.command()
@click.option('--dataset_id', type=int, required=True)
@click.option('--name', type=str, required=True)
@click.option('--directory', type=click.Path(exists=True), required=True)
def add_topicmodel(dataset_id, name, directory):
    id = len(Dataset.query.get(dataset_id).topicmodels) + 1
    topicmodel = TopicModel(id, dataset_id, name)
    db.session.add(topicmodel)
    db.session.commit()
    print('TopicModel #{} for Dataset #{} added'.format(id, dataset_id))


@cli.command()
@click.option('--name', type=str, required=True)
@click.option('--directory', type=click.Path(exists=True), required=True)
def generate_sample_dataset(name, directory):
    # Handle documents.

    documents = [Document('arXiv paper'),
                 Document('non-arXiv paper'),
                 Document('other paper')]

    with open(os.path.join(directory, 'documents.csv'), 'w') as csvfile:
        for idx, document in enumerate(documents):
            # csvfile.writerow()
            print(idx, document)


    # Handle terms.

    terms = [Term('machine'),
             Term('learning'),
             Term('is'),
             Term('superior')]

    with open(os.path.join(directory, 'documents.csv'), 'w') as csvfile:
        for idx, document in enumerate(documents):
            # csvfile.writerow()
            print(idx, document)


if __name__ == '__main__':
    cli()
