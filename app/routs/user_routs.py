# app/routes/user_routes.py
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def user_list():
    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/user/<int:user_id>')
def user_detail(user_id):
    user = User.query.get(user_id)
    return render_template('user_detail.html', user=user)

# Add routes for create, update, and delete here
