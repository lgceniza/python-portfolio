from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from forms import AddTaskForm, UpdateTaskForm
from utils import parse_form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mtm23gt8a7gtuaz7g8282ga'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(100), unique=True, nullable=False)
  date = db.Column(db.String(20), nullable=False)

@app.route('/', methods=['GET'])
def home():
  addform = AddTaskForm()
  tasks = Task.query.all()

  return render_template('index.html', form=addform, tasks=tasks, num_tasks=len(tasks))

@app.route('/add', methods=['POST'])
def add_task():
  formdata = parse_form(request.get_data(as_text=True))
  task = Task(
      description = formdata['task'],
      date = datetime.today().strftime("%B %d, %Y")
    )

  db.session.add(task)
  db.session.commit()

  return redirect(url_for('home'))

@app.route('/todo', methods=['GET'])
def task():
  tasks = Task.query.all()
  todo = Task.query.get(request.args.get('id'))
  form = UpdateTaskForm(task = todo.description)

  return render_template('update.html', form=form, task_id=todo.id, tasks=tasks, num_tasks=len(tasks))

@app.route('/update', methods=['POST'])
def update_task():
  formdata = parse_form(request.get_data(as_text=True))
  todo = Task.query.get(request.args.get('id'))
  todo.description = formdata['task']
  db.session.commit()
  
  return redirect(url_for('home'))

@app.route('/delete', methods=['GET'])
def delete_task():
  task = Task.query.get(request.args.get('id'))
  db.session.delete(task)
  db.session.commit()

  return redirect(url_for('home'))

if __name__ == "__main__":
  app.run(debug=True)
