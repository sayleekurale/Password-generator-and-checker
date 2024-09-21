from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

password_history = []
max_passwords = 20

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.choice(characters) for _ in range(length))

    global password_history
    password_history.append(password)
    password_history = password_history[-max_passwords:]
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    data = request.get_json()
    length = data.get('length', 12)
    include_uppercase = data.get('include_uppercase', True)
    include_lowercase = data.get('include_lowercase', True)
    include_numbers = data.get('include_numbers', True)
    include_symbols = data.get('include_symbols', True)

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
    return jsonify({'password': password})

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password', '')

    length = len(password)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_symbols = any(not c.isalnum() for c in password)

    strength = ''
    if length < 8:
        strength = "Weak: Your password should be at least 8 characters long."
    elif (has_uppercase and has_lowercase and has_numbers and has_symbols) or (length >= 12 and has_uppercase and has_lowercase and has_numbers):
        strength = "Strong: Great password!"
    else:
        strength = "Medium: Consider a mix of character types."
    
    return jsonify({'strength': strength})

@app.route('/view_history', methods=['GET'])
def view_history():
    return jsonify({'history': password_history})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    global password_history
    password_history = []  # Clear the history
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)

