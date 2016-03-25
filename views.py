# -*- encoding: utf-8 ---------------------------------------------------------


from operator import attrgetter

from serve import *
from models import *


@app.route('/')
@app.route('/index.html')
def index():
    datasets = Dataset.query.all()
    return render_template('index.html', datasets=datasets)


@app.route('/dataset/<int:dataset_id>/topic_model/<int:topic_model_id>')
def topic_model(dataset_id, topic_model_id):
    dataset = Dataset.query.get(dataset_id)
    topic_model = TopicModel.query.get((dataset_id, topic_model_id))
    top_ten_topics = sorted(topic_model.topics,
        key=attrgetter('probability'), reverse=True)[:10]
    return render_template('topic_model.html',
        dataset=dataset,
        topic_model=topic_model,
        top_ten_topics=top_ten_topics)


@app.route('/dataset/<int:dataset_id>/topic_model/<int:topic_model_id>'
           '/browse_topics.html')
def browse_topics(dataset_id, topic_model_id):
    dataset = Dataset.query.get(dataset_id)
    topic_model = TopicModel.query.get((dataset_id, topic_model_id))
    topics = topic_model.topics
    return render_template('browse_topics.html',
        dataset=dataset,
        topic_model=topic_model,
        topics=topics)


@app.route('/dataset/<int:dataset_id>/topic_model/<int:topic_model_id>'
           '/topic/<int:topic_id>')
def topic(dataset_id, topic_model_id, topic_id):
    return render_template('topic.html',
        dataset=Dataset.query.get(dataset_id),
        topic_model=TopicModel.query.get((dataset_id, topic_model_id)),
        topic=Topic.query.get((dataset_id, topic_model_id, topic_id)))


@app.route('/dataset/<int:dataset_id>/topic_model/<int:topic_model_id>/'
           'term/<int:term_id>')
def term(dataset_id, topic_model_id, term_id):
    term = Term.query.filter_by(dataset_id=dataset_id, id=term_id).all()[0]
    return render_template('term.html',
        dataset=Dataset.query.get(dataset_id),
        topic_model=TopicModel.query.get((dataset_id, topic_model_id)),
        term=term)


@app.route('/dataset/<int:dataset_id>/topic_model/<int:topic_model_id>/'
           'document/<int:document_id>')
def document(dataset_id, topic_model_id, document_id):
    return render_template('document.html',
        dataset=Dataset.query.get(dataset_id),
        topic_model=TopicModel.query.get((dataset_id, topic_model_id)))
