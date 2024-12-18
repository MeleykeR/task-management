from flask import Blueprint, request, jsonify
from app.services.task_service import create_task, edit_task, delete_task, update_task_status

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/tasks', methods=['POST'])
def create():
    data = request.get_json()
    task = create_task(data)
    return jsonify(task), 201

@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
def edit(task_id):
    data = request.get_json()
    task = edit_task(task_id, data)
    return jsonify(task)

@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    delete_task(task_id)
    return '', 204

@task_routes.route('/tasks/<int:task_id>/status', methods=['PUT'])
def update_status(task_id):
    status = request.get_json()['status']
    task = update_task_status(task_id, status)
    return jsonify(task)
