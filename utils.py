from flask import Flask, jsonify, request
from configs import users as usersConfig

app = Flask(__name__)

client = app.test_client()

@app.route('/users', methods=['GET'])
def users():
    return jsonify(usersConfig)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    item = next((x for x in usersConfig if x['id'] == user_id), None)
    params = request.json
    if not item:
        return {'error': 'Not found user'}, 400
    return jsonify(users[user_id])

if __name__ == '__main__':
    app.run()