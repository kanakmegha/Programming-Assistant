# RAG-Based LLM App with Flask and Docker

## Overview

This project is a **Programming Assistant** powered by a **Retrieval-Augmented Generation (RAG)** approach using a large language model (LLM). The app allows users to ask programming-related questions, retrieve relevant information from documents, and provide detailed, context-aware responses.

### Key Technologies
- **Flask**: A lightweight Python web framework used to serve the application.
- **Docker**: Used to containerize the application for easy deployment and portability.
- **RAG (Retrieval-Augmented Generation)**: Combines traditional search-based retrieval with modern language generation techniques to produce context-aware answers.
- **Vext AI**: A service for processing queries based on input documents and a keyword-based system to generate accurate responses.

## Features

- **Query Processing**: Users can input programming-related queries, and the app will provide contextually relevant answers.
- **Document Search**: The app fetches relevant documents based on keywords or user input.
- **Deployment with Docker**: The application can be easily deployed locally or on any server with Docker support.
- **Web Interface**: A user-friendly interface built using HTML and JavaScript to interact with the assistant.

## Requirements

- **Python 3.x**: Ensure you have Python installed on your local machine.
- **Docker**: To containerize and deploy the application.
- **Vext API Key**: You'll need an API key from [Vext AI](https://vextapp.com/) to process user queries using RAG techniques.

## Setup and Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/kanakmegha/Programming-Assistant.git
cd Programming-Assistant
```
## 2. Install Python Dependencies

Ensure that you have **pip** installed, then install the required Python libraries:

```bash
pip install -r requirements.txt
```
## 3. Set Up Vext AI API

You need an API key from **Vext AI** to use their keyword-based document retrieval system. Obtain the API key and set it in your environment variables or directly in the `app.py` file as shown below:

```python
API_KEY = "your_vext_api_key_here"
```
## 4. Running the Flask App Locally

Once you've set up your environment, you can run the Flask application locally by executing the following command:

```bash
python app.py
```
This will start a local development server, typically available at http://127.0.0.1:5000/. You can access the web interface and test the programming assistant from there.
## 5. Deploying with Docker

If you want to deploy the app using **Docker** for portability, follow these steps:

### Build the Docker Image

Run the following command to build a Docker image:

```bash
docker build -t programming-assistant .
```
Once the image is built, run it in a Docker container:
```bash
docker run -p 8001:5000 programming-assistant
```
This will make the Flask application accessible at http://localhost:8001 in your browser.
