from flask import Flask, jsonify
from flask_cors import CORS
from UI.UserUI import UserUI

app = Flask(__name__)
cors = CORS(app)
user_ui = UserUI()


@app.route('/main/', methods=['GET', 'POST'])
def main():
    return 'Running'


@app.route('/postUser/<string:user>', methods=['POST'])
def post_user(user):
    user_ui.post_user(user)

    return jsonify({
        'Status': 200,
        'Message': 'Success',
    })


@app.route('/getUserExists/<string:username>', methods=['GET'])
def username_exists(username):

    exists = str(user_ui.attribute_exists('User', username))

    return jsonify({
        'Status': 200,
        'Exists': exists,
    })

@app.route('/getEmailExists/<string:email>', methods=['GET'])
def email_exists(email):

    exists = str(user_ui.attribute_exists('Email', email))

    return jsonify({
        'Status': 200,
        'Exists': exists,
    })


if __name__ == "__main__":
    app.run(port=8888)
