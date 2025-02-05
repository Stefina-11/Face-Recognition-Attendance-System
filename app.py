from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
from main import main_bp  # Import Blueprint from main.py

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Register the blueprint from main.py
app.register_blueprint(main_bp)

# Dummy credentials for login example
USERNAME = 'admin'
PASSWORD_HASH = hashlib.sha256('pass'.encode()).hexdigest()

@app.route('/')
def home():
    return render_template('login.html')  # Render the login form page

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Hash the entered password for comparison
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if credentials are correct
    if username == USERNAME and password_hash == PASSWORD_HASH:
        session['logged_in'] = True
        return redirect(url_for('main.main_page'))  # Redirect to main page if login is successful
    else:
        error_message = "Invalid credentials, please try again."
        return render_template('login.html', error_message=error_message)  # Display error message

if __name__ == '__main__':
    app.run(debug=True)
