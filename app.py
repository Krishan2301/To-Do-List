from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lists to store task data
tasks = []
priorities = []
statuses = []

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, priorities=priorities, statuses=statuses)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    priority = request.form.get('priority')
    tasks.append(task)
    priorities.append(priority)
    statuses.append('Incomplete')
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        priorities.pop(task_id)
        statuses.pop(task_id)
    return redirect(url_for('index'))

# Route to update task status
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        status = request.form.get('status')
        statuses[task_id] = 'Completed' if status == '1' else 'Incomplete'
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
