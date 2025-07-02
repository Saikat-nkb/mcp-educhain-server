# EduChain MCP Server 

This project is a Flask-based MCP server for the AI Intern Assignment, simulating EduChain integration with three educational tools/resources for Claude Desktop.

## Features

- **generate_mcq:** Generate multiple-choice questions for any topic.
- **generate_lesson_plan:** Generate a lesson plan for any topic.
- **generate_flashcards:** Generate flashcards for any topic (bonus tool).

## Setup

1. Clone the repo.
2. Install dependencies:
   pip install -r requirements.txt
3. Run the server:
   python main.py
4. Configure Claude Desktop using claude_desktop_config.json.

## Testing

- Use Postman or Claude Desktop to send POST requests to `http://127.0.0.1:5000/mcp` with JSON like:
