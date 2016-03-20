# -*- encoding: utf-8 ---------------------------------------------------------


import csv
import os.path

from serve import db
from models import *


def create():
    db.create_all()
    print('Database created')


def clear():
    db.drop_all()
    print('Database cleared')


def write_to_csv(filename, column_names, columns):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(column_names)
        for row in columns:
            writer.writerow(row)


def generate_sample_dataset(directory):
    for model in dataset_models:
        print(model)


def generate_sample_topicmodel(directory):
    for model in topicmodel_models:
        print(model)


def add_dataset(name, directory):
    dataset = Dataset(name=name)
    db.session.add(dataset)
    db.session.commit()
    print('Dataset #{} added'.format(dataset.id))

    for model in dataset_models:
        print(model)
    


def add_topicmodel(name, directory, dataset_id):
    id = len(Dataset.query.get(dataset_id).topicmodels) + 1
    topicmodel = TopicModel(id=id, name=name, dataset=dataset_id)
    db.session.add(topicmodel)
    db.session.commit()
    print('TopicModel #{} for Dataset #{} added'.format(id, dataset_id))

    for model in topicmodel_models:
        print(model)
