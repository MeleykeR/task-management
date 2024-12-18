from flask import Blueprint, request, jsonify
from app.services.assignee_service import assign_task, unassign_task, get_assignee_task_count

assignee_routes = Blueprint('assignee_routes', __name__)

@assignee_routes.route('/tasks/<int:task_id>/assign', methods=['POST'])
def assign(task_id):
    assignees = request.get_json()['assignees']
    assign_task(task_id, assignees)
    return '', 200

@assignee_routes.route('/tasks/<int:task_id>/assign', methods=['DELETE'])
def unassign(task_id):
    assignees = request.get_json()['assignees']
    unassign_task(task_id, assignees)
    return '', 200

@assignee_routes.route('/reports/assignee/<int:assignee_id>/tasks', methods=['GET'])
def assignee_task_count(assignee_id):
    count = get_assignee_task_count(assignee_id)
    return jsonify({'task_count': count})
