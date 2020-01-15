# imports an app object (created in __init__py  Flask(__name__))
from app import app, db 
from flask import render_template, request, redirect
from app.models import User, Task

@app.route('/tasks')
def index():
    user= User.query.get(1)
    tasks = user.tasks
    return render_template('index.html', title='Home', user=user, tasks=tasks)

@app.route('/tasks', methods=['POST'])
def create():
    user= User.query.get(1)
    taskTitle = request.form['title']
    taskDesc = request.form['description']
    newTask = Task(title=taskTitle, description=taskDesc, user=user)
    db.session.add(newTask)
    db.session.commit()
    return redirect('/tasks')

