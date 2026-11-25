from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    text = request.args.get("q", "<b>Hello</b>")
    return render_template("safe_demo.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
