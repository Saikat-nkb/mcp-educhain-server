# EduChain MCP Server 

This project is a Flask-based MCP server for the AI Intern Assignment, simulating EduChain integration with three educational tools/resources for Claude Desktop.

## Features

- **generate_mcq:** Generate multiple-choice questions for any topic.
- **generate_lesson_plan:** Generate a lesson plan for any topic.
- **generate_flashcards:** Generate flashcards for any topic (bonus tool).

## Project structure
 mcp-educhain-server/
├── main.py
├── educhain_tools.py
├── requirements.txt
├── claude_desktop_config.json
├── Sample_Responses.txt
└── README.md



## Setup Instructions

1. Clone the repo.
 

2. Install dependencies:
   pip install -r requirements.txt

3. Run the server:
   python main.py

4. Configure Claude Desktop using claude_desktop_config.json.

## Testing
- Use Postman or Claude Desktop to send POST requests to `http://127.0.0.1:5000/mcp` with JSON like:
```
{
  "tool": "generate_mcq",
  "params": {
    "topic": "Python loops",
    "level": "Beginner",
    "num": 5
  }
}
```
## With Claude Desktop
Place claude_desktop_config.json in the same directory as Claude Desktop or import it via the app's settings.

Start the MCP server (python main.py).

In Claude Desktop, use commands like:

Generate 5 multiple-choice questions on Python loops.

Provide a lesson plan for teaching algebra.

Generate flashcards on World War II.

## See Sample_Responses.txt for example commands and responses.

## Deployment (Render.com)
You can deploy this project for free using Render.com:

Push all files to GitHub .

Sign up or log in at Render.com.

Create a new Web Service:

Build command:

```
text:
 pip install -r requirements.txt
 ```

Start command:

```
text
gunicorn main:app
```

Connect your GitHub repo.

Deploy and get your public URL.

Access your app:
The web frontend will be available at the root URL, and the MCP API at /mcp.


## Citation
This project uses and references the following resources:

## EduChain Library:
https://github.com/satvik314/educhain

## MCP Protocol Documentation:
Claude Desktop MCP Protocol (if you used any SDK or docs)
