import React, { useState, useEffect } from 'react';

function TodoApp() {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState('');

    // Fetch tasks from the backend
    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/todo')
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data) => {
                setTasks(data.tasks);
            })
            .catch((error) => {
                console.error('There was an error fetching tasks!', error);
            });
    }, []);

    // Function to handle adding a new task
    const handleAddTask = () => {
        if (newTask.trim() === '') return;

        fetch('http://127.0.0.1:5000/api/todo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ task: newTask }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(() => {
                setTasks((prevTasks) => [...prevTasks, newTask]);
                setNewTask('');
            })
            .catch((error) => {
                console.error('There was an error adding the task!', error);
            });
    };

    // Function to handle deleting a task
    const handleDeleteTask = (taskId) => {
        fetch(`http://127.0.0.1:5000/api/todo/${taskId}`, {
            method: 'DELETE',
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(() => {
                setTasks((prevTasks) => prevTasks.filter((_, index) => index !== taskId));
            })
            .catch((error) => {
                console.error('There was an error deleting the task!', error);
            });
    };

    return (
        <div>
        <h1 className="header">To-Do List</h1>
        <div className="container">
            <form className="add-task-form" onSubmit={(e) => {
                e.preventDefault();
                handleAddTask();
            }}>
                <input
                    type="text"
                    value={newTask}
                    onChange={(e) => setNewTask(e.target.value)}
                    placeholder="Enter a new task"
                />
                <button type="submit">Add Task</button>
            </form>
            <ol>
                {tasks.map((task, index) => (
                    <li key={index}>
                        {task}
                        <button className="delete-task" onClick={() => handleDeleteTask(index)}>Delete</button>
                    </li>
                ))}
            </ol>
        </div>
    </div>
    );
}

export default TodoApp;
