/* ============================================================
   EXPERIMENT 10 - To-Do List application logic
   JS concepts used: variables & datatypes, arrays, objects,
   functions, events, string methods, if-else, forEach/filter,
   DOM manipulation, form validation and localStorage.
   ============================================================ */

// ---------- State: an array of task objects ----------
var tasks = [];
var currentFilter = 'all';

// ---------- DOM element references ----------
var form = document.getElementById('task-form');
var input = document.getElementById('task-input');
var errorBox = document.getElementById('form-error');
var list = document.getElementById('task-list');
var stats = document.getElementById('task-stats');
var storageNote = document.getElementById('storage-note');
var clearBtn = document.getElementById('clear-completed');

// ---------- localStorage with in-memory fallback ----------
var storageOK = true;
function loadTasks() {
    try {
        var saved = localStorage.getItem('todo-tasks');
        if (saved !== null) {
            tasks = JSON.parse(saved);          // JSON string -> array of objects
        }
    } catch (e) {
        storageOK = false;
        storageNote.textContent = '(storage blocked: tasks kept for this session only)';
        tasks = [];
    }
}
function saveTasks() {
    if (!storageOK) return;
    try {
        localStorage.setItem('todo-tasks', JSON.stringify(tasks));
    } catch (e) {
        storageOK = false;
        storageNote.textContent = '(storage blocked: tasks kept for this session only)';
    }
}

// ---------- Validation: non-empty, no duplicates ----------
function validateTask(text) {
    var value = text.trim();                                  // string method: trim()
    if (value.length === 0) {
        return { ok: false, message: 'Task cannot be empty. Please type something.' };
    }
    if (value.length < 3) {
        return { ok: false, message: 'Task must be at least 3 characters long.' };
    }
    var duplicate = tasks.some(function (t) {
        return t.text.toLowerCase() === value.toLowerCase();  // string method: toLowerCase()
    });
    if (duplicate) {
        return { ok: false, message: 'This task already exists in your list.' };
    }
    return { ok: true, value: value };
}

// ---------- Add a new task ----------
function addTask(text) {
    var task = {
        id: Date.now(),                 // unique id (number)
        text: text,                     // string
        completed: false,               // boolean
        createdAt: new Date().toLocaleString()
    };
    tasks.push(task);                   // array method: push
    saveTasks();
    render();
}

// ---------- Toggle the completed flag of a task ----------
function toggleTask(id) {
    tasks.forEach(function (task) {
        if (task.id === id) {
            task.completed = !task.completed;   // if-else logic via boolean flip
        }
    });
    saveTasks();
    render();
}

// ---------- Delete a task by id ----------
function deleteTask(id) {
    tasks = tasks.filter(function (task) {      // array method: filter
        return task.id !== id;
    });
    saveTasks();
    render();
}

// ---------- Remove every completed task ----------
function clearCompleted() {
    tasks = tasks.filter(function (task) {
        return task.completed === false;
    });
    saveTasks();
    render();
}

// ---------- Render the list according to the active filter ----------
function render() {
    list.innerHTML = '';

    var visible = tasks.filter(function (task) {
        if (currentFilter === 'active')    return task.completed === false;
        if (currentFilter === 'completed') return task.completed === true;
        return true;                                        // 'all'
    });

    if (visible.length === 0) {
        var li = document.createElement('li');
        li.className = 'empty-msg';
        li.textContent = currentFilter === 'all'
            ? 'No tasks yet. Add your first task above!'
            : 'No ' + currentFilter + ' tasks to show.';
        list.appendChild(li);
    } else {
        visible.forEach(function (task) {
            var li = document.createElement('li');
            if (task.completed) li.className = 'completed';

            // checkbox
            var checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'toggle';
            checkbox.checked = task.completed;
            checkbox.addEventListener('change', function () { toggleTask(task.id); });

            // text
            var span = document.createElement('span');
            span.className = 'task-text';
            span.textContent = task.text;

            // timestamp
            var time = document.createElement('span');
            time.className = 'task-time';
            time.textContent = task.createdAt;

            // delete button
            var del = document.createElement('button');
            del.type = 'button';
            del.className = 'delete-btn';
            del.textContent = '\u2716';
            del.title = 'Delete task';
            del.addEventListener('click', function () { deleteTask(task.id); });

            li.appendChild(checkbox);
            li.appendChild(span);
            li.appendChild(time);
            li.appendChild(del);
            list.appendChild(li);
        });
    }

    updateStats();
}

// ---------- Footer statistics ----------
function updateStats() {
    var total = tasks.length;
    var done = tasks.filter(function (t) { return t.completed; }).length;
    var pending = total - done;
    stats.textContent = total + ' task' + (total === 1 ? '' : 's') +
                        '  |  ' + pending + ' active  |  ' + done + ' completed';
}

// ---------- Event: form submit (add task) ----------
form.addEventListener('submit', function (event) {
    event.preventDefault();
    var result = validateTask(input.value);
    if (!result.ok) {
        errorBox.textContent = result.message;
        input.classList.add('invalid');
        input.focus();
        return;
    }
    errorBox.textContent = '';
    input.classList.remove('invalid');
    addTask(result.value);
    input.value = '';
    input.focus();
});

// ---------- Event: filter buttons (event delegation) ----------
document.querySelectorAll('.filter-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
        document.querySelectorAll('.filter-btn').forEach(function (b) {
            b.classList.remove('active');
        });
        btn.classList.add('active');
        currentFilter = btn.getAttribute('data-filter');
        render();
    });
});

// ---------- Event: clear completed tasks ----------
clearBtn.addEventListener('click', clearCompleted);

// ---------- Start the application ----------
loadTasks();
render();
