# llama-chabot
---

This project is an AI-powered chatbot built using a Python backend, Reflex for the frontend, and Llama model from TogetherAI accessed via APIs. The chatbot is designed to engage users in conversations, answer questions, and provide assistance based on the advanced capabilities of the Llama language model.

## Features

- **AI-Powered Responses**: The chatbot is powered by the Llama language model, which provides intelligent and context-aware responses.
- **Python Backend**: The backend handles the communication between the chatbot and the Llama model API, managing conversation state and processing user input.
- **Reflex Frontend**: The frontend is built with Reflex, providing a simple, interactive, and user-friendly interface for users to chat with the AI.
- **Real-Time Conversations**: Users can chat with the AI in real-time, receiving quick and relevant responses to their queries.

## Prerequisites

Before you start, make sure you have the following:

- Python 3.8 or higher
- An API key from TogetherAI for accessing the Llama model
- Reflex library installed (frontend)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-chatbot.git
cd chatapp
```

### 2. Set up the Python environment:

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

Ensure you have the required packages for API requests, Llama model, and any additional dependencies for the backend.

### 4. Set up TogetherAI API:

- Go to [TogetherAI](https://together.ai) and create an account to obtain your API key.
- Add the API key to your environment variables or the config file:

```bash
export TOGETHER_API_KEY="your-api-key-here"  # On Windows, use set instead of export
```

### 5. Running the App in dev mode:

To start the Reflex app, run:

```bash
reflex run --loglevel debug
```

This will launch the Reflex app in your browser, where you can interact with the chatbot.

## Usage

1. Open the app in your browser (typically at `http://localhost:5004`).
2. Type a message in the input field to interact with the AI.
3. The chatbot will respond with a text message powered by the Llama model via the API.