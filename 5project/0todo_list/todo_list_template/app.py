from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory todo list
todos = []
todo_id_counter = 1

@app.route('/')
def index():
    return render_template('todo.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    global todo_id_counter
    text = request.form.get('text', '').strip()
    if text:
        todos.append({
            'id': todo_id_counter,
            'text': text,
            'done': False
        })
        todo_id_counter += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
