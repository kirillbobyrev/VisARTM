# -*- encoding: utf-8 ---------------------------------------------------------


from serve import *
from models import *


@app.route('/')
@app.route('/index.html')
def index():
    datasets = Dataset.query.all()
    return render_template('index.html', datasets=datasets)


@app.route('/dataset/<int:dataset_id>')
def dataset(dataset_id):
    return render_template('dataset.html',
                           dataset=Dataset.query.get(dataset_id))


@app.route('/dataset/<int:dataset_id>/topicmodel/<int:topicmodel_id>')
def topicmodel(dataset_id, topicmodel_id):
    return render_template('topic_model.html',
                           topicmodel=TopicModel.query.get((dataset_id,
                                                            topicmodel_id)))
