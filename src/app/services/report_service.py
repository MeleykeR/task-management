from app.models import db, Task
from datetime import datetime

def get_overdue_tasks():
    today = datetime.today().date()
    overdue_tasks = Task.query.filter(Task.due_date < today, Task.status != 'Completed').all()
    return [{'id': task.id, 'title': task.title, 'due_date': task.due_date} for task in overdue_tasks]

def get_task_summary():
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter_by(status='Completed').count()
    pending_tasks = Task.query.filter_by(status='Pending').count()
    overdue_tasks = Task.query.filter(Task.due_date < datetime.today().date(), Task.status != 'Completed').count()
    return {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks
    }
