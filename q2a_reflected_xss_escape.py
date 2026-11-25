from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/unsafe")
def unsafe():
    name = request.args.get("name", "Guest")
    return f"<h3>Unsafe Output: Hello {name}</h3>"

@app.route("/safe")
def safe():
    name = request.args.get("name", "Guest")
    return f"<h3>Safe Output: Hello {escape(name)}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
