import os
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Todo

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    if request.method == "POST":
        taskName = request.form['task']
        todo = Todo(taskName)
        db.session.add(todo)
        db.session.commit()
    return render_template('index.html', todos=Todo.query.all())


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()