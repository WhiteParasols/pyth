const todoList = document.getElementById('todoList');
const addTodo = document.getElementById('addTodo');
const userInput = document.getElementById('userInput');

function renderTodo(todo) {
    const li = document.createElement('li');
    li.dataset.id = todo.id;
    if (todo.done) li.classList.add('strikethrough');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = todo.done;

    const span = document.createElement('span');
    span.textContent = todo.text;

    const button = document.createElement('button');
    button.textContent = 'delete';

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(button);
    todoList.appendChild(li);
}

async function loadTodos() {
    const res = await fetch('/api/todos');
    const data = await res.json();
    todoList.innerHTML = '';
    data.forEach(renderTodo);
}

addTodo.addEventListener('click', async () => {
    const text = userInput.value.trim();
    if (!text) return;
    const res = await fetch('/api/todos', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text})
    });
    const newTodo = await res.json();
    renderTodo(newTodo);
    userInput.value = '';
});

userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') addTodo.click();
});

todoList.addEventListener('click', async (e) => {
    const li = e.target.closest('li');
    const id = li.dataset.id;

    if (e.target.tagName === 'BUTTON') {
        await fetch(`/api/todos/${id}`, { method: 'DELETE' });
        li.remove();
    }

    if (e.target.tagName === 'INPUT') {
        await fetch(`/api/todos/${id}`, { method: 'PUT' });
        li.classList.toggle('strikethrough');
    }
});

loadTodos();
