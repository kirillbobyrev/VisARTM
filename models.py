from serve import db


# -----------------------------------------------------------------------------
# Dataset-related models
# -----------------------------------------------------------------------------


class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))

    documents = db.relationship('Document')
    terms = db.relationship('Term')
    topic_models = db.relationship('TopicModel')


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    abstract = db.Column(db.Text)
    content = db.Column(db.Text)

    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)

    document_topics = db.relationship('DocumentTopic',
                                      primaryjoin='and_(Document.id =='
                                      'DocumentTopic.document_id,'
                                      'Document.dataset_id =='
                                      'DocumentTopic.dataset_id)',
                                      backref='document')
    document_terms = db.relationship('DocumentTerm',
                                     primaryjoin='and_(Document.id =='
                                     'DocumentTerm.document_id,'
                                     'Document.dataset_id =='
                                     'DocumentTerm.dataset_id)',
                                     backref='document')
    similar_documents_l = db.relationship('DocumentSimilarity',
                                          primaryjoin='and_(Document.id == '
                                          'DocumentSimilarity.document_l_id,'
                                          'Document.dataset_id =='
                                          'DocumentSimilarity.dataset_id)',
                                          backref='document_l')
    similar_documents_r = db.relationship('DocumentSimilarity',
                                          primaryjoin='and_(Document.id =='
                                          'DocumentSimilarity.document_r_id,'
                                          'Document.dataset_id =='
                                          'DocumentSimilarity.dataset_id)',
                                          backref='document_r')
    document_assessment = db.relationship('DocumentAssessment',
                                          primaryjoin='and_(Document.id =='
                                          'DocumentAssessment.document_id,'
                                          'Document.dataset_id =='
                                          'DocumentAssessment.dataset_id)',
                                          backref='document')
    document_to_topic_assessments = db.relationship(
        'DocumentToTopicAssessment',
        primaryjoin='and_(Document.id =='
        'DocumentToTopicAssessment.'
        'document_id, Document.dataset_id =='
        'DocumentToTopicAssessment.'
        'dataset_id)',
        backref='document')
    document_to_term_assessments = db.relationship('DocumentToTermAssessment',
                                                   primaryjoin='and_(Document.'
                                                   'id =='
                                                   'DocumentToTermAssessment.'
                                                   'document_id,'
                                                   'Document.dataset_id =='
                                                   'DocumentToTermAssessment.'
                                                   'dataset_id)',
                                                   backref='document')
    document_to_document_l_assessments = db.relationship(
        'DocumentToDocumentAssessment',
        primaryjoin='and_(Document.id =='
        'DocumentToDocumentAssessment.'
        'document_l_id,'
        'Document.dataset_id =='
        'DocumentToDocumentAssessment.'
        'dataset_id)',
        backref='document_l')
    document_to_document_r_assessments = db.relationship(
        'DocumentToDocumentAssessment',
        primaryjoin='and_(Document.id =='
        'DocumentToDocumentAssessment.'
        'document_r_id, Document.dataset_id =='
        'DocumentToDocumentAssessment.'
        'dataset_id)',
        backref='document_r')


class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)

    topic_terms = db.relationship('TopicTerm',
                                  primaryjoin='and_(Term.id =='
                                  'TopicTerm.term_id,'
                                  'Term.dataset_id == TopicTerm.dataset_id)',
                                  backref='term')
    document_terms = db.relationship('DocumentTerm',
                                     primaryjoin='and_(Term.id =='
                                     'DocumentTerm.term_id,'
                                     'Term.dataset_id =='
                                     'DocumentTerm.dataset_id)',
                                     backref='term')
    similar_terms_l = db.relationship('TermSimilarity',
                                      primaryjoin='and_(Term.id =='
                                      'TermSimilarity.term_l_id,'
                                      'Term.dataset_id =='
                                      'TermSimilarity.dataset_id)',
                                      backref='term_l')
    similar_terms_r = db.relationship('TermSimilarity',
                                      primaryjoin='and_(Term.id =='
                                      'TermSimilarity.term_r_id,'
                                      'Term.dataset_id =='
                                      'TermSimilarity.dataset_id)',
                                      backref='term_r')
    term_assessment = db.relationship('TermAssessment',
                                      primaryjoin='and_(Term.id =='
                                      'TermAssessment.term_id,'
                                      'Term.dataset_id =='
                                      'TermAssessment.dataset_id)',
                                      backref='term')
    term_to_topic_assessments = db.relationship('TermToTopicAssessment',
                                                primaryjoin='and_(Term.id =='
                                                'TermToTopicAssessment.'
                                                'term_id,'
                                                'Term.dataset_id =='
                                                'TermToTopicAssessment.'
                                                'dataset_id)',
                                                backref='term')
    term_to_document_assessments = db.relationship('TermToDocumentAssessment',
                                                   primaryjoin='and_(Term.id'
                                                   '=='
                                                   'TermToDocumentAssessment.'
                                                   'term_id,'
                                                   'Term.dataset_id =='
                                                   'TermToDocumentAssessment.'
                                                   'dataset_id)',
                                                   backref='term')
    term_to_term_l_assessments = db.relationship('TermToTermAssessment',
                                                 primaryjoin='and_(Term.id =='
                                                 'TermToTermAssessment.'
                                                 'term_l_id,'
                                                 'Term.dataset_id =='
                                                 'TermToTermAssessment.'
                                                 'dataset_id)',
                                                 backref='term_l')
    term_to_term_r_assessments = db.relationship('TermToTermAssessment',
                                                 primaryjoin='and_(Term.id =='
                                                 'TermToTermAssessment.'
                                                 'term_r_id,'
                                                 'Term.dataset_id =='
                                                 'TermToTermAssessment.'
                                                 'dataset_id)',
                                                 backref='term_r')


class DocumentTerm(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)

    count = db.Column(db.Integer)


dataset_models = [Document, Term, DocumentTerm]


# -----------------------------------------------------------------------------
# TopicModel-related models
# -----------------------------------------------------------------------------


class TopicModel(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(120))

    topics = db.relationship('Topic',
                             primaryjoin='and_(TopicModel.id =='
                             'Topic.topic_model_id,'
                             'TopicModel.dataset_id == Topic.dataset_id)')


class Topic(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(120))
    probability = db.Column(db.Float)
    is_background = db.Column(db.Boolean)

    topic_terms = db.relationship('TopicTerm',
                                  primaryjoin='and_(Topic.id =='
                                  'TopicTerm.topic_id,'
                                  'Topic.dataset_id == TopicTerm.dataset_id,'
                                  'Topic.topic_model_id =='
                                  'TopicTerm.topic_model_id)',
                                  backref='topic')
    document_topics = db.relationship('DocumentTopic',
                                      primaryjoin='and_(Topic.id =='
                                      'DocumentTopic.topic_id,'
                                      'Topic.dataset_id =='
                                      'DocumentTopic.dataset_id,'
                                      'Topic.topic_model_id =='
                                      'DocumentTopic.topic_model_id)',
                                      backref='topic')
    similar_topics_l = db.relationship('TopicSimilarity',
                                       primaryjoin='and_(Topic.id =='
                                       'TopicSimilarity.topic_l_id,'
                                       'Topic.dataset_id =='
                                       'TopicSimilarity.dataset_id,'
                                       'Topic.topic_model_id =='
                                       'TopicSimilarity.topic_model_id)',
                                       backref='topic_l')
    similar_topics_r = db.relationship('TopicSimilarity',
                                       primaryjoin='and_(Topic.id =='
                                       'TopicSimilarity.topic_r_id,'
                                       'Topic.dataset_id =='
                                       'TopicSimilarity.dataset_id,'
                                       'Topic.topic_model_id =='
                                       'TopicSimilarity.topic_model_id)',
                                       backref='topic_r')
    topic_assessment = db.relationship('TopicAssessment',
                                       primaryjoin='and_(Topic.id =='
                                       'TopicAssessment.topic_id,'
                                       'Topic.dataset_id =='
                                       'TopicAssessment.dataset_id)',
                                       backref='topic')
    topic_to_term_assessments = db.relationship('TopicToTermAssessment',
                                                primaryjoin='and_(Topic.id =='
                                                'TopicToTermAssessment.'
                                                'topic_id,'
                                                'Topic.dataset_id =='
                                                'TopicToTermAssessment.'
                                                'dataset_id)',
                                                backref='topic')
    topic_to_document_assessments = db.relationship(
        'TopicToDocumentAssessment',
        primaryjoin='and_(Topic.id'
        '=='
        'TopicToDocumentAssessment.'
        'topic_id,'
        'Topic.dataset_id =='
        'TopicToDocumentAssessment.'
        'dataset_id)',
        backref='topic')
    topic_to_topic_l_assessments = db.relationship('TopicToTopicAssessment',
                                                   primaryjoin='and_(Topic.id'
                                                   '=='
                                                   'TopicToTopicAssessment.'
                                                   'topic_l_id,'
                                                   'Topic.dataset_id =='
                                                   'TopicToTopicAssessment.'
                                                   'dataset_id)',
                                                   backref='topic_l')
    topic_to_topic_r_assessments = db.relationship('TopicToTopicAssessment',
                                                   primaryjoin='and_(Topic.id'
                                                   '=='
                                                   'TopicToTopicAssessment.'
                                                   'topic_r_id,'
                                                   'Topic.dataset_id =='
                                                   'TopicToTopicAssessment.'
                                                   'dataset_id)',
                                                   backref='topic_r')


class TopicTerm(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    prob_wt = db.Column(db.Float)
    prob_tw = db.Column(db.Float)


class DocumentTopic(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    prob_dt = db.Column(db.Float)
    prob_td = db.Column(db.Float)


class TopicSimilarity(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    topic_l_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    topic_r_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    similarity = db.Column(db.Float)


class TermSimilarity(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    term_l_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    term_r_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    similarity = db.Column(db.Float)


class DocumentSimilarity(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    document_l_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    document_r_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    similarity = db.Column(db.Float)


topicmodel_models = [Topic, TopicTerm, DocumentTopic, TopicSimilarity,
                     TermSimilarity, DocumentSimilarity]


# -----------------------------------------------------------------------------
# Assesment-relatetd models
# -----------------------------------------------------------------------------

class TopicAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    score = db.Column(db.Integer)


class TopicToTermAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    score = db.Column(db.Integer)


class TopicToDocumentAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    score = db.Column(db.Integer)


class TopicToTopicAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    topic_l_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    topic_r_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    score = db.Column(db.Integer)


class TermAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    score = db.Column(db.Integer)


class TermToTopicAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    score = db.Column(db.Integer)


class TermToDocumentAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    score = db.Column(db.Integer)


class TermToTermAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    term_l_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    term_r_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    score = db.Column(db.Integer)


class DocumentAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    score = db.Column(db.Integer)


class DocumentToTopicAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    topic_model_id = db.Column(db.Integer, db.ForeignKey(
        'topic_model.id'), primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey(
        'topic.id'), primary_key=True)
    score = db.Column(db.Integer)


class DocumentToTermAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey(
        'term.id'), primary_key=True)
    score = db.Column(db.Integer)


class DocumentToDocumentAssessment(db.Model):
    dataset_id = db.Column(db.Integer, db.ForeignKey(
        'dataset.id'), primary_key=True)
    document_l_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    document_r_id = db.Column(db.Integer, db.ForeignKey(
        'document.id'), primary_key=True)
    score = db.Column(db.Integer)
