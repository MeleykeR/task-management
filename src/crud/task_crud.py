from sqlalchemy.orm import Session
from src.models.task import Task

# CREATE: Add a new task
def create_task(db: Session, title: str, description: str = ""):
    new_task = Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# READ: Get all tasks
def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

# READ: Get a specific task by ID
def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# UPDATE: Update a task by ID
def update_task(db: Session, task_id: int, title: str = None, description: str = None, completed: bool = None):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if completed is not None:
        task.completed = completed
    db.commit()
    db.refresh(task)
    return task

# DELETE: Delete a task by ID
def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task
