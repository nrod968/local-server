import sqlite3 as sql
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from constants import MONTHS

db_name = 'needles.db'

app = Flask(__name__)
with open('local_server.pub') as keyfile:
    app.config['SECRET_KEY'] = keyfile.read()

@app.route('/')
def index():
    conn = get_db_connection()
    needles = conn.execute('SELECT * FROM needles').fetchall()
    conn.close()
    return render_template('index.html', needles=needles)

@app.route('/<int:needle_id>')
def needle(needle_id):
    needle = get_needle(needle_id)
    return render_template('needle.html', needle=needle)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO needles (title, content) VALUES (?, ?)',
                        (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html', months=MONTHS)

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    needle = get_needle(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE needles SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', needle=needle)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    needle = get_needle(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM needles WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(needle['title']))
    return redirect(url_for('index'))

def get_db_connection():
    conn = sql.connect(db_name)
    conn.row_factory = sql.Row
    return conn

def get_needle(needle_id):
    conn = get_db_connection()
    needle = conn.execute('SELECT * FROM needles WHERE id = ?',
                        (needle_id,)).fetchone()
    conn.close()
    if needle is None:
        abort(404)
    return needle