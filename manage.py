# -*- encoding: utf-8 ---------------------------------------------------------


import csv
import os.path
import random

from serve import db
from models import *


def create():
    db.create_all()
    print('db.create_all()')


def clear():
    db.drop_all()
    print('db.drop_all()')


def write_to_csv(filename, column_names, columns):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(column_names)
        for row in columns:
            writer.writerow(row)


def generate_sample(directory, topic_count=100, document_count=100,
                    term_count=100):
    # Generate Document table.
    filename = os.path.join(directory, Document.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'title', 'abstract'])
        for idx in range(document_count):
            writer.writerow([idx, 'document-{}'.format(idx),
                'document-{} abstract'.format(idx)])

    # Generate Term table.
    filename = os.path.join(directory, Term.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'text'])
        for idx in range(term_count):
            writer.writerow([idx, 'term-{}'.format(idx)])


    # Generate DocumentTerm table.
    filename = os.path.join(directory, DocumentTerm.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['document', 'term', 'count'])
        for document_id in range(document_count):
            for term_id in range(term_count):
                writer.writerow([document_id, term_id, random.randint(0, 10)])

    # Generate Topic table.
    filename = os.path.join(directory, Topic.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'title', 'probability', 'is_background'])
        for idx in range(topic_count):
            writer.writerow([idx, 'topic-{}'.format(idx), random.random(),
                             random.choice([1, 0])])

    # Generate TopicTerm table.
    filename = os.path.join(directory, TopicTerm.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['topic', 'term', 'prob_wt', 'prob_tw'])
        for topic_id in range(topic_count):
            for term_id in range(term_count):
                writer.writerow([topic_id, term_id, random.random(),
                                 random.random()])

    # Generate DocumentTopic table.
    filename = os.path.join(directory, DocumentTopic.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['document', 'topic', 'prob_dt', 'prob_td'])
        for document_id in range(document_count):
            for topic_id in range(topic_count):
                writer.writerow([document_id, topic_id, random.random(),
                                 random.random()])


    # Generate TopicSimilarity table.
    filename = os.path.join(directory, TopicSimilarity.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['topic_l', 'topic_r', 'similarity'])
        for topic_l in range(topic_count):
            for topic_r in range(topic_count):
                writer.writerow([topic_l, topic_r, random.random()])


    # Generate TermSimilarity table.
    filename = os.path.join(directory, TermSimilarity.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['term_l', 'term_r', 'similarity'])
        for term_l in range(topic_count):
            for term_r in range(topic_count):
                writer.writerow([term_l, term_r, random.random()])


    # Generate DocumentSimilarity table.
    filename = os.path.join(directory,
                            DocumentSimilarity.__tablename__ + '.csv')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['docment_l', 'document_r', 'similarity'])
        for document_l in range(document_count):
            for document_r in range(document_count):
                writer.writerow([document_l, document_r, random.random()])


def read_from_csv(model, directory, initial_dict):
    filename = os.path.join(directory, model.__tablename__ + '.csv')

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        argument_names = next(reader)
        for row in reader:
            arguments = dict(zip(argument_names, row))
            arguments.update(initial_dict)
            item = model(**arguments)
            db.session.add(item)

    db.session.commit()


def add_dataset(name, directory):
    dataset = Dataset(name=name)
    db.session.add(dataset)
    db.session.commit()
    print('Dataset #{} added'.format(dataset.id))

    for model in dataset_models:
        read_from_csv(model, directory, {'dataset' : dataset.id})
    print('Data for Dataset #{} loaded successfully'.format(dataset.id))


def add_topicmodel(name, directory, dataset_id):
    id = len(Dataset.query.get(dataset_id).topicmodels) + 1
    dataset = Dataset.query.get(dataset_id)
    topicmodel = TopicModel(id=id, name=name, dataset=dataset.id)
    db.session.add(topicmodel)
    db.session.commit()
    print('TopicModel #{} for Dataset #{} added'.format(topicmodel.id,
                                                        dataset.id))

    for model in topicmodel_models:
        read_from_csv(model, directory,
            {'dataset' : dataset.id, 'topicmodel' : topicmodel.id})
    print('Data for TopicModel #{} loaded successfully'.format(topicmodel.id))
