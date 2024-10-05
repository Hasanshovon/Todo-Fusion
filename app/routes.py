from app import app
from flask import render_template

@app.route("/")
def hello_world():
    return render_template("index.html")
# create another route
@app.route("/todo")
def todo():
    return render_template("todo.html")