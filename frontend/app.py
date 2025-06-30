from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    user_input = request.form['user_input']
    response = requests.post(
        'http://localhost:3001/api/data',
        json={'input': user_input}
    )
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
