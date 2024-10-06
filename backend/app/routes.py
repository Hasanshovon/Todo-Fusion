from app import app
from flask import jsonify, request
from app.services import get_tasks, add_task, delete_task

@app.route("/api/todo", methods=["GET"])
def get_all_tasks():
    tasks = get_tasks()
    return jsonify({"tasks": tasks})

@app.route("/api/todo", methods=["POST"])
def add_new_task():
    task = request.json.get("task")
    if task:
        add_task(task)
        return jsonify({"message": "Task added successfully"}), 201
    return jsonify({"error": "Task is required"}), 400

@app.route("/api/todo/<int:task_id>", methods=["DELETE"])
def delete_task_by_id(task_id):
    if delete_task(task_id):
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"error": "Invalid task ID"}), 400
