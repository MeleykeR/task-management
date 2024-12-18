from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base  # Assuming Base is defined in src.database

# User Table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Hash passwords in real apps

    tasks = relationship("Task", secondary="task_assignments", back_populates="assignees")
    comments = relationship("Comment", back_populates="user")
    history = relationship("TaskHistory", back_populates="user")

# Task Table
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

    assignments = relationship("TaskAssignment", back_populates="task")
    assignees = relationship("User", secondary="task_assignments", back_populates="tasks")
    comments = relationship("Comment", back_populates="task")
    history = relationship("TaskHistory", back_populates="task")

# Task Assignment Table
class TaskAssignment(Base):
    __tablename__ = "task_assignments"

    task_id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    task = relationship("Task", back_populates="assignments")
    user = relationship("User", back_populates="tasks")

# Comment Table
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    task = relationship("Task", back_populates="comments")
    user = relationship("User", back_populates="comments")

# Task History Table
class TaskHistory(Base):
    __tablename__ = "task_history"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    status = Column(String, nullable=False)
    changed_by = Column(Integer, ForeignKey("users.id"))
    changed_at = Column(String, nullable=False)

    task = relationship("Task", back_populates="history")
    user = relationship("User", back_populates="history")
