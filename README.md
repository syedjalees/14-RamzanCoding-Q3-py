Chatbot using Google Gemini API and Chainlit

This project implements a simple chatbot that uses Google Gemini API for generative responses and Chainlit for the chat interface. The chatbot interacts with users and generates content based on their input.

Features

Generative AI Responses: Uses Google Gemini API for text generation.

Real-Time Chat: Built with Chainlit for an interactive chat interface.

Secure API Key Management: API key is loaded from a .env file.

Installation
Clone the repository and navigate to the project directory:

git clone <https://github.com/syedjalees/14-RamzanCoding-Q3-py>

cd <14-RamzanCoding-Q3-py>

Set up a virtual environment:
python -m venv venv

source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate  # For Windows

Install dependencies:
pip install chainlit google-generativeai python-dotenv

Create a .env file and add your Gemini API key:

GEMINI_API_KEY=your_google_api_key_here

Run the chatbot:

chainlit run <main.py>

Code Overview

Environment Variables: Loads the API key from .

env using dotenv.

Chat Start: Greets the user when the chat starts.

Message Handling: Sends user input to the Gemini API and returns the generated response.

Example .env File

GEMINI_API_KEY=your_api_key_here

License
This project is licensed under the MIT License.