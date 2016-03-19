# -*- encoding: utf-8 ---------------------------------------------------------


import sys
import inspect

from serve import db


# -----------------------------------------------------------------------------
# Dataset-related models
# -----------------------------------------------------------------------------


class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    topicmodels = db.relationship('TopicModel', backref='dataset',
                                  lazy='dynamic') 
    def __init__(self, name):
        self.name = name


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))

    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'))


    def __init__(self, title):
        self.title = title


class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))

    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'))


    def __init__(self, text):
        self.text = text

dataset_models = (Document, Term)


# -----------------------------------------------------------------------------
# TopicModel-related models
# -----------------------------------------------------------------------------


class TopicModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'))

    def __init__(self, name, dataset_id):
        self.name = name
        self.dataset_id = dataset_id


topicmodel_models = ()
