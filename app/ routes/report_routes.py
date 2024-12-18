from flask import Blueprint, jsonify
from app.services.report_service import get_overdue_tasks, get_task_summary

report_routes = Blueprint('report_routes', __name__)

@report_routes.route('/reports/overdue', methods=['GET'])
def overdue_tasks():
    tasks = get_overdue_tasks()
    return jsonify(tasks)

@report_routes.route('/reports/summary', methods=['GET'])
def task_summary():
    summary = get_task_summary()
    return jsonify(summary)
