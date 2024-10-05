from app import app
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# create another route
@app.route("/todo")
def todo():
    return "<p>Todo Page</p>"