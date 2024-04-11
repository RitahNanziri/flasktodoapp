from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['POST'])
def edit_todo(index):
    if request.method == 'POST':
        new_todo = request.form['todo']
        todos[index] = new_todo
        return redirect(url_for('index'))
    return jsonify({'success': False}), 400

@app.route('/delete/<int:index>', methods=['POST'])
def delete_todo(index):
    if request.method == 'POST':
        del todos[index]
        return redirect(url_for('index'))
    return jsonify({'success': False}), 400




if __name__ == '__main__':
    app.run(debug=True)
