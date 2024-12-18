import random
from datetime import datetime, timedelta
from faker import Faker
from app import db
from app.models import Task, User

fake = Faker()

# Function to generate random users (assignees)
def generate_users(num_users=5):
    users = []
    for _ in range(num_users):
        user = User(
            name=fake.name(),
            email=fake.email()
        )
        users.append(user)
    db.session.add_all(users)
    db.session.commit()
    return users

# Function to generate random tasks
def generate_tasks(num_tasks=10):
    tasks = []
    users = User.query.all()  # Assuming users have been created already

    for _ in range(num_tasks):
        task = Task(
            title=fake.bs(),
            description=fake.text(),
            due_date=fake.date_between(start_date='today', end_date='+30d'),
            created_at=datetime.utcnow(),
            status=random.choice(['Pending', 'In Progress', 'Completed'])
        )

        # Assign random users to the task
        num_assignees = random.randint(1, 3)
        assignees = random.sample(users, num_assignees)
        task.assignees = assignees  # Assuming the relationship is set up in SQLAlchemy

        tasks.append(task)

    db.session.add_all(tasks)
    db.session.commit()
    return tasks

# Function to generate a full set of dummy data (users + tasks)
def generate_dummy_data():
    print("Generating users...")
    generate_users(5)  # Create 5 users

    print("Generating tasks...")
    generate_tasks(10)  # Create 10 tasks

    print("Dummy data generated successfully.")

# Function to reset the database and generate fresh dummy data
def reset_and_generate_data():
    # Reset all tasks and users
    Task.query.delete()
    User.query.delete()
    db.session.commit()

    # Generate fresh dummy data
    generate_dummy_data()
