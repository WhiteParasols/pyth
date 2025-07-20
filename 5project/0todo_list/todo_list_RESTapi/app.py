from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
todos = []

@app.route('/')
def index():
    return render_template('todo.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = {
        'id': len(todos) + 1,
        'text': data['text'],
        'done': False
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id']!=todo_id]
    return '',204

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            return jsonify(todo)
    return jsonify({'error':'Not found'}), 404

if __name__=='__main__':
    app.run(debug=True)