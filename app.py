from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bonjour à tous, Ceci est une simple application conteneurisée avec Docker par Catherine!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
