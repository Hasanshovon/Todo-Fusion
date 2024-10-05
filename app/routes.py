from app import app
from flask import render_template, request, redirect, url_for
from app.services import get_tasks, add_task, delete_task


"""
@app.route("/")
def hello_world():
    return render_template("index.html")
"""
@app.route("/", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "add":
            # Handle adding a task
            task = request.form.get("task")
            if task:
                add_task(task)

        elif action == "delete":
            # Handle deleting a task
            task_id = request.form.get("task_id")
            if task_id is not None:
                delete_task(int(task_id))

        # After adding or deleting, redirect to refresh the list
        return redirect(url_for("todo"))

    # For GET request, render the todo list
    tasks = get_tasks()
    return render_template("todo.html", tasks=tasks)
