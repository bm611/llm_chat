# Gemini Chat App

A simple chat application using Google's Gemini AI model.

## Installation

1. Clone the repository:
   ```
   git clone <repository name>
   cd <repository name>
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Set up the Gemini API key:
   - Obtain an API key from [Google AI Studio](https://aistudio.google.com)
   - Set the environment variable:
     ```
     export GEMINI_API_KEY=your_api_key_here
     ```
     On Windows, use `set` instead of `export`.

4. Run the application:
   ```
   reflex run
   ```

5. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Enter your prompt in the text box and click "Submit".
2. To ask a follow-up question, simply enter it in the text box and submit again.
3. To start a new chat, click the "Clear" button.

## TODO

- Implement chat history functionality
