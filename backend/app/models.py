# app/models.py

# A simple in-memory list to store tasks for now
tasks = []

# Alternatively, if you use SQLAlchemy for database management:
# from flask_sqlalchemy import SQLAlchemy
# from app import app
# db = SQLAlchemy(app)
#
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     completed = db.Column(db.Boolean, default=False)
