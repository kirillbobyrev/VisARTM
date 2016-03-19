# -*- encoding: utf-8 ---------------------------------------------------------


from serve import *
from models import *


@app.route('/')
@app.route('/index.html')
def index():
    datasets = Dataset.query.all()
    topicmodels = TopicModel.query.all()
    return render_template('index.html',
                           datasets=datasets,
                           topicmodels=topicmodels)
