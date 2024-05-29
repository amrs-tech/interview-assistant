# Interview Assistant

Interview Assistant is an AI-powered web application designed to assist with interview preparation by providing intelligent responses to user queries. This project leverages a Flask web server to handle user interactions and integrates with a chatbot model to generate responses using the Groq SDK for the Groq LLM API service, which utilizes the LLaMA3 7B model.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Routes](#routes)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with Interview Assistant, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/amrs-tech/interview-assistant.git
    cd interview-assistant
    ```

2. **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```bash
    python app.py
    ```

## Usage

Once the application is running, open your web browser and navigate to `http://127.0.0.1:5000/`. You will be greeted with the homepage where you can start interacting with the AI-powered assistant.

## Project Structure

The project has the following structure:
```
interview-assistant/
├── static/
├── templates/
│   └── index.html
├── chatbot.py
├── app.py
├── requirements.txt
└── README.md
```

- `static/`: Contains CSS and JS code for rendering styles and scripts.
- `templates/`: Contains HTML templates for rendering web pages.
- `chatbot.py`: Contains the logic for interacting with the chatbot model.
- `app.py`: The main Flask application file.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: Documentation for the project.

## Routes

### `GET /`
Renders the homepage with chatbox.

### `POST /get_response`
Receives a user's message, sends it to the chatbot model, and returns the model's response.

## API Reference

### `call_model_api(message)`
- **Description**: Sends a user's message to the chatbot model and returns the model's response.
- **Parameters**: 
  - `message` (str): The user's message.
- **Returns**: 
  - `response` (str): The response from the chatbot model.

## Dependencies

- **Flask**: Web framework for Python.
- **Groq SDK**: Python SDK for the Groq LLM API service.
- **LLaMA3 7B Model**: The underlying LLM used in the API.

To install the Groq SDK, ensure it is listed in your `requirements.txt`:
```
flask
groq
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
