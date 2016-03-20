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


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    abstract = db.Column(db.Text)

    dataset = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)


class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    dataset = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)


class DocumentTerm(db.Model):
    dataset = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    document = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    term = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)

    count = db.Column(db.Integer)
    

dataset_models = [Term, Document, DocumentTerm]


# -----------------------------------------------------------------------------
# TopicModel-related models
# -----------------------------------------------------------------------------


class TopicModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(120))

    dataset = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)

    topics = db.relationship('Topic')


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(120))
    probabilities = db.Column(db.Float)
    is_background = db.Column(db.Boolean)

    topicmodel = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)


class TopicTerm(db.Model):
    topicmodel = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    term = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    topic = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    prob_wt = db.Column(db.Float)
    prob_tw = db.Column(db.Float)


class DocumentTopic(db.Model):
    topicmodel = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    document = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    topic = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    prob_dt = db.Column(db.Float)
    prob_td = db.Column(db.Float)


class TopicSimilarity(db.Model):
    topicmodel = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    topic_l = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    topic_r = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    similarity = db.Column(db.Float)


class TermSimilarity(db.Model):
    topicmodel = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    term_l = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    term_r = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    similarity = db.Column(db.Float)


topicmodel_models = [Topic, TopicTerm, DocumentTopic, TopicSimilarity,
    TermSimilarity]
