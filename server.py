from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Rate limiting configuration
RATE_LIMIT = 20  # Maximum number of attempts
TIME_WINDOW = 30  # Time in seconds


login_attempts = {}

def is_rate_limited(ip):
    current_time = time.time()
    if ip not in login_attempts:
        login_attempts[ip] = []
    attempts = login_attempts[ip]
    attempts = [timestamp for timestamp in attempts if current_time - timestamp < TIME_WINDOW]
    login_attempts[ip] = attempts
    return len(attempts) >= RATE_LIMIT

@app.route('/login', methods=['POST'])
def login():
    ip = request.remote_addr
    if is_rate_limited(ip):
        return "Rate limit exceeded. Try again later.", 429
    
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "tina" and password == "password!1":
        return "Login successful", 200
    else:
        # TO  Record the login attempt
        if ip in login_attempts:
            login_attempts[ip].append(time.time())
        else:
            login_attempts[ip] = [time.time()]
        return "Login failed", 401

if __name__ == "__main__":
    app.run(debug=True)

