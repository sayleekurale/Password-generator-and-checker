# Password Generator And Checker Flask App 🔐

This is a simple Flask web application that generates secure passwords and checks their strength. The app includes functionality to view and manage a history of generated passwords.

## Features ✒️✒️

- Generate passwords with customizable options (length, uppercase, lowercase, numbers, symbols).
- Check the strength of a given password.
- View the history of generated passwords.
- Clear the password history.

## Technologies Used 💻

- Python
- Flask
- HTML/CSS for frontend
- JavaScript for asynchronous requests

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-generator-flask-app.git
   cd password-generator-flask-app
   ```

2. Install the required packages:
   ```bash
   pip install Flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

### Generate a Password

1. On the homepage, you can select options to customize your password generation.
2. Click the "Generate" button to create a new password.

### Check Password Strength

1. Enter a password in the provided input field.
2. Click the "Check Strength" button to evaluate the password.

### View Password History

- Click on the "View History" button to see a list of previously generated passwords.

### Clear Password History

- You can clear the password history by clicking the "Clear History" button.

## API Endpoints

- `POST /generate_password`: Generates a new password with specified options.
- `POST /check_password`: Checks the strength of a given password.
- `GET /view_history`: Retrieves the history of generated passwords.
- `POST /clear_history`: Clears the password history.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [Python](https://www.python.org/) - The programming language used for this application. 

Feel free to reach out if you have any questions or suggestions!
