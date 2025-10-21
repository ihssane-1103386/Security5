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
            key = Fernet.generate_key().decode() #fernet genereert een key (decode om het van een byte naar een string te brengen)
        else:
            text = request.form["text"] #tekst van de gebruiker wordt opgehaald om te versleutelen.
            key = request.form["key"] #de key wordt opgehaald om de tekst te kunnen versleutelen.
            fernet = Fernet(key.encode()) #tekst wordt versleuteld
            if action == "encrypt":
                result = fernet.encrypt(text.encode()).decode() #resultaat van encryptie wordt weergegeven
            elif action == "decrypt": #iemand wil tekst ontsleutelen
                result = fernet.decrypt(text.encode()).decode() #resultaat ontsleutelen van de versleutelde tekst wordt weergegeven

    return render_template("index.html", result=result, key=key)

if __name__ == "__main__":
    app.run(debug=True)
