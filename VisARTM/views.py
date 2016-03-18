from serve import *

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
