from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins CI/CD Pipeline!"

@app.route('/status')
def status():
    return "The application is running fine!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
