from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "CS6006NX Assignment 2 Web App - Successful Deployment!"

if __name__ == '__main__':
    app.run()