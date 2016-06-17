from flask import render_template
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
                           topic_model=TopicModel.query.get((dataset_id,
                                                             topic_model_id)),
                           topic=Topic.query.get((dataset_id,
                                                  topic_model_id, topic_id)))


@app.route('/dataset/<int:dataset_id>/topic_model/<int:topic_model_id>/'
           'term/<int:term_id>')
def term(dataset_id, topic_model_id, term_id):
    term = Term.query.filter_by(dataset_id=dataset_id, id=term_id).all()[0]
    topic_terms = [topic_term for topic_term in term.topic_terms
                   if topic_term.topic_model_id == topic_model_id]
    similar_terms_l = [similar_term for similar_term in term.similar_terms_l
                       if similar_term.topic_model_id == topic_model_id]
    return render_template('term.html',
                           dataset=Dataset.query.get(dataset_id),
                           topic_model=TopicModel.query.get((dataset_id,
                                                             topic_model_id)),
                           term=term,
                           topic_terms=topic_terms,
                           similar_terms_l=similar_terms_l)


@app.route('/dataset/<int:dataset_id>/topic_model/<int:topic_model_id>/'
           'document/<int:document_id>')
def document(dataset_id, topic_model_id, document_id):
    document = Document.query.get((document_id, dataset_id))
    document_topics = [document_topic for document_topic
                       in document.document_topics if
                       document_topic.topic_model_id == topic_model_id]
    document_similarities = [similarity for similarity in
                             document.similar_documents_l if
                             similarity.topic_model_id == topic_model_id]
    return render_template('document.html',
                           dataset=Dataset.query.get(dataset_id),
                           topic_model=TopicModel.query.get((dataset_id,
                                                             topic_model_id)),
                           document=document,
                           document_topics=document_topics,
                           document_similarities=document_similarities)
