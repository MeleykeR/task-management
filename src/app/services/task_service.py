from app.models import db, Task, Assignee
from datetime import datetime

def create_task(data):
    task = Task(title=data['title'], description=data['description'], due_date=datetime.strptime(data['due_date'], '%Y-%m-%d'))
    db.session.add(task)
    db.session.commit()
    return task

def edit_task(task_id, data):
    task = Task.query.get(task_id)
    task.title = data['title']
    task.description = data['description']
    task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
    db.session.commit()
    return task

def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

def update_task_status(task_id, status):
    task = Task.query.get(task_id)
    task.status = status
    db.session.commit()
    return task
