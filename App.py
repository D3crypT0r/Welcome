import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phno TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phno = request.form['phno']
        password = request.form['pwd']
        
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        try:
            c.execute("INSERT INTO users (name, phno, password) VALUES (?, ?, ?)", (name, phno, password))
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Phone number already exists. Please try another.', 'danger')
            return render_template('register.html')  

        finally:
            conn.close()

    return render_template('register.html')  


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phno = request.form['phno']
        password = request.form['pwd']

        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE phno=? AND password=?", (phno, password))
        user = c.fetchone()
        
        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('index')) 
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return render_template('login.html')  

        conn.close()

    return render_template('login.html')  

if __name__ == '__main__':
    init_db()  
    app.run(debug=True)
