from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Todo


todo_bp = Blueprint('todo_bp', __name__, template_folder='templates')


@todo_bp.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@todo_bp.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')
    if content:
        new_task = Todo(content=content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('todo_bp.index'))


@todo_bp.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo_bp.index'))
