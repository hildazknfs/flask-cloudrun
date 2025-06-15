from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learning DevOps"},
    {"id": 2, "task": "Making CI/CD Pipeline"},
    {"id": 3, "task": "Testing Push on GitHub Actions"}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)