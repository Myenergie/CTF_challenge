from flask import Flask, request, render_template_string, send_from_directory
import sqlite3

app = Flask(__name__)

def check_credentials(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password)) # SQL Injection vulnerability here
    result = c.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if check_credentials(request.form['username'], request.form['password']):
            return render_template_string("Success! Download your reward <a href='/reward'>here</a>.")
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template_string('''
            <form method="post">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Submit"><br>
            </form>
            {{error}}
        ''', error=error)

@app.route('/reward', methods=['GET'])
def reward():
    return send_from_directory(directory='.', filename='reward')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
