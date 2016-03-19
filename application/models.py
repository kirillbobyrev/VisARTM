# -*- encoding: utf-8 ---------------------------------------------------------


from serve import db


class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Dataset {}'.format(name)
