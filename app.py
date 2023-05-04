from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)


class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)

  def __repr__(self):
    return f'{self.title}'


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    task_title = request.form['title']
    new_task = Task(title=task_title)

    try:
      db.session.add(new_task)
      db.session.commit()
      flash('Task added successfully', 'success')
      return redirect(url_for('index'))
    except:
      flash('Error adding task', 'danger')
      return redirect(url_for('index'))

  tasks = Task.query.order_by(Task.id).all()
  return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
  task_to_delete = Task.query.get_or_404(id)

  try:
    db.session.delete(task_to_delete)
    db.session.commit()
    flash('Task deleted successfully', 'success')
    return redirect(url_for('index'))
  except:
    flash('Error deleting task', 'danger')
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  task_to_update = Task.query.get_or_404(id)

  if request.method == 'POST':
    task_to_update.title = request.form['title']

    try:
      db.session.commit()
      flash('Task updated successfully', 'success')
      return redirect(url_for('index'))
    except:
      flash('Error updating task', 'danger')
      return redirect(url_for('index'))

  return render_template('update.html', task=task_to_update)


if __name__ == "__main__":
  app.run(debug=True)
