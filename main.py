"""
main.py

MCP Server for EduChain Assignment

This script sets up a Flask-based MCP server exposing educational tools
that generate multiple-choice questions, lesson plans, and flashcards.
The server is designed for integration with Claude Desktop.

Author: SAIKAT CHATTERJEE
Citations:
- EduChain: https://github.com/satvik314/educhain
- MCP Protocol Documentation

"""

from flask import Flask, request, jsonify,render_template
from educhain_tools import (
    generate_mcq,
    generate_lesson_plan,
    generate_flashcards
)

# Initialize Flask app
app = Flask(__name__)

# Map tool/resource names to their handler functions
TOOL_MAP = {
    "generate_mcq": generate_mcq,
    "generate_lesson_plan": generate_lesson_plan,
    "generate_flashcards": generate_flashcards
}
#for frontend  rendering

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/mcp", methods=["POST"])
def mcp_endpoint():
    """
    Main MCP endpoint for handling tool/resource requests.

    Expects a JSON payload:
    {
        "tool": "<tool_name>",
        "params": { ... }
    }

    Returns:
        JSON response with generated educational content or error message.
    """
    data = request.get_json(force=True)
    tool = data.get("tool")
    params = data.get("params", {})

    if tool not in TOOL_MAP:
        return jsonify({"error": f"Tool '{tool}' not found."}), 400

    try:
        # Call the appropriate tool/resource function
        result = TOOL_MAP[tool](params)
        return jsonify(result)
    except Exception as e:
        # Log the exception in production for debugging
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the server on localhost:5000
    app.run(host="127.0.0.1", port=5000, debug=True)
