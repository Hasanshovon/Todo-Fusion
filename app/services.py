from app.models import tasks


# add task 
def add_task(task):
    tasks.append(task)

# get task
def get_tasks():
    return tasks


# delete task

def delete_task(task):
    tasks.remove(task)