from flask import render_template, request, jsonify
from operator import attrgetter

from serve import *
from models import *
from app import db


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
    topic = Topic.query.get((dataset_id, topic_model_id, topic_id))
 
    topic_score = 0
    for topic_assessment in topic.topic_assessment:
        topic_score = topic_assessment.score

    topic_to_term_scores = [0] * len(Term.query.all())
    for topic_to_term_assessment in topic.topic_to_term_assessments:
        topic_to_term_scores[topic_to_term_assessment.term_id] = topic_to_term_assessment.score

    topic_to_document_scores = [0] * len(Document.query.all())
    for topic_to_document_assessment in topic.topic_to_document_assessments:
        topic_to_document_scores[topic_to_document_assessment.document_id] = topic_to_document_assessment.score

    topic_to_topic_scores = [0] * len(Topic.query.all())
    for topic_to_topic_assessment in topic.topic_to_topic_l_assessments:
        topic_to_topic_scores[topic_to_topic_assessment.topic_r_id] = topic_to_topic_assessment.score

    return render_template('topic.html',
                           dataset=Dataset.query.get(dataset_id),
                           topic_model=TopicModel.query.get((dataset_id,
                                                             topic_model_id)),
                           topic=topic,
                           topic_score=topic_score,
                           topic_to_term_scores=topic_to_term_scores,
                           topic_to_document_scores=topic_to_document_scores,
                           topic_to_topic_scores=topic_to_topic_scores)


@app.route('/dataset/<int:dataset_id>/topic_model/<int:topic_model_id>/'
           'term/<int:term_id>')
def term(dataset_id, topic_model_id, term_id):
    term = Term.query.filter_by(dataset_id=dataset_id, id=term_id).all()[0]
    topic_terms = [topic_term for topic_term in term.topic_terms
                   if topic_term.topic_model_id == topic_model_id]
    similar_terms_l = [similar_term for similar_term in term.similar_terms_l
                       if similar_term.topic_model_id == topic_model_id]

    term_score = 0
    for term_assessment in term.term_assessment:
        term_score = term_assessment.score

    term_to_topic_scores = [0] * len(Topic.query.all())
    for term_to_topic_assessment in term.term_to_topic_assessments:
        term_to_topic_scores[term_to_topic_assessment.topic_id] = term_to_topic_assessment.score

    term_to_document_scores = [0] * len(Document.query.all())
    for term_to_document_assessment in term.term_to_document_assessments:
        term_to_document_scores[term_to_document_assessment.document_id] = term_to_document_assessment.score

    term_to_term_scores = [0] * len(Term.query.all())
    for term_to_term_assessment in term.term_to_term_l_assessments:
        term_to_term_scores[term_to_term_assessment.term_r_id] = term_to_term_assessment.score

    return render_template('term.html',
                           dataset=Dataset.query.get(dataset_id),
                           topic_model=TopicModel.query.get((dataset_id,
                                                             topic_model_id)),
                           term=term,
                           topic_terms=topic_terms,
                           similar_terms_l=similar_terms_l,
                           term_score=term_score,
                           term_to_topic_scores=term_to_topic_scores,
                           term_to_document_scores=term_to_document_scores,
                           term_to_term_scores=term_to_term_scores)


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

    document_score = 0
    for document_assessment in document.document_assessment:
        document_score = document_assessment.score

    document_to_topic_scores = [0] * len(Topic.query.all())
    for document_to_topic_assessment in document.document_to_topic_assessments:
        document_to_topic_scores[document_to_topic_assessment.topic_id] = document_to_topic_assessment.score

    document_to_term_scores = [0] * len(Term.query.all())
    for document_to_term_assessment in document.document_to_term_assessments:
        document_to_term_scores[document_to_term_assessment.term_id] = document_to_term_assessment.score

    document_to_document_scores = [0] * len(Document.query.all())
    for document_to_document_assessment in document.document_to_document_l_assessments:
        document_to_document_scores[document_to_document_assessment.document_r_id] = document_to_document_assessment.score

    return render_template('document.html',
                           dataset=Dataset.query.get(dataset_id),
                           topic_model=TopicModel.query.get((dataset_id,
                                                             topic_model_id)),
                           document=document,
                           document_topics=document_topics,
                           document_similarities=document_similarities,
                           document_score=document_score,
                           document_to_topic_scores=document_to_topic_scores,
                           document_to_term_scores=document_to_term_scores,
                           document_to_document_scores=document_to_document_scores)


# assessment stuff
@app.route('/assess', methods=['POST'])
def assess():
    print(request.form)
    assessment = eval(request.form['class_name'] + '({}, score={})'.format(
        request.form['arg_list'], request.form['score']))
    eval(request.form['class_name'] + '.query.filter_by({})'
        .format(request.form['arg_list']) + '.delete()')
    db.session.add(assessment)
    db.session.commit()
    return jsonify(success=True)
