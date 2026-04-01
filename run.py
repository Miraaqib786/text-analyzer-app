from flask import Flask, render_template, request
from app.analyzer import analyze_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    result = None
    if request.method == "POST":
        text = request.form.get("text", "")
        result = analyze_text(text)
    return render_template("index.html", text=text, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)