from app.models import db, Task, Assignee, TaskAssignee

def assign_task(task_id, assignee_ids):
    task = Task.query.get(task_id)
    for assignee_id in assignee_ids:
        assignee = Assignee.query.get(assignee_id)
        task.assignees.append(assignee)
    db.session.commit()

def unassign_task(task_id, assignee_ids):
    task = Task.query.get(task_id)
    for assignee_id in assignee_ids:
        assignee = Assignee.query.get(assignee_id)
        task.assignees.remove(assignee)
    db.session.commit()

def get_assignee_task_count(assignee_id):
    assignee = Assignee.query.get(assignee_id)
    return len(assignee.tasks)
