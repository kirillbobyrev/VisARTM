# -*- encoding: utf-8 ---------------------------------------------------------


import sys
import inspect

from serve import db


# -----------------------------------------------------------------------------
# Dataset-related models
# -----------------------------------------------------------------------------


class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))

    documents = db.relationship('Document')
    terms = db.relationship('Term')
    topicmodels = db.relationship('TopicModel')

    def __init__(self, name):
        self.name = name 


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataset = db.Column(db.Integer, db.ForeignKey('dataset.id'), primary_key=True)
    title = db.Column(db.Text)


    def __init__(self, id, dataset, title):
        self.id = id
        self.dataset = dataset
        self.title = title
        

class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataset = db.Column(db.Integer, db.ForeignKey('dataset.id'), primary_key=True)
    text = db.Column(db.Text)

    def __init__(self, id, dataset, title):
        self.id = id
        self.dataset = dataset
        self.text = text


dataset_models = (Document, Term)


# -----------------------------------------------------------------------------
# TopicModel-related models
# -----------------------------------------------------------------------------


class TopicModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    dataset = db.Column(db.Integer, db.ForeignKey('dataset.id'), primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, id, dataset, name):
        self.id = id
        self.dataset = dataset
        self.name = name

    
topicmodel_models = ()
