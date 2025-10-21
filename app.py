from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    key = ""
    if request.method == "POST":
        action = request.form["action"]
        if action == "generate_key":
            key = Fernet.generate_key().decode()
        else:
            text = request.form["text"]
            key = request.form["key"]
            fernet = Fernet(key.encode())
            if action == "encrypt":
                result = fernet.encrypt(text.encode()).decode()
            elif action == "decrypt":
                result = fernet.decrypt(text.encode()).decode()

    return render_template("index.html", result=result, key=key)

if __name__ == "__main__":
    app.run(debug=True)
