from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)
    status = db.Column(db.String(50), default='Pending')
    assignees = db.relationship('Assignee', secondary='task_assignee', back_populates='tasks')

class Assignee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    tasks = db.relationship('Task', secondary='task_assignee', back_populates='assignees')

class TaskAssignee(db.Model):
    __tablename__ = 'task_assignee'
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), primary_key=True)
    assignee_id = db.Column(db.Integer, db.ForeignKey('assignee.id'), primary_key=True)
