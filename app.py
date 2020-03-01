import json
from flask import Flask, request, make_response
from unfurl_message import start_login, finish_login, unfurl

app = Flask(__name__)


@app.route('/', methods=['POST'])
def unfurl_call():
    event = {
        'body': json.dumps(request.json)
    }
    unfurl_response = unfurl(event, {})
    return make_response(unfurl_response['body'],
                         unfurl_response['statusCode'])


@app.route('/login', methods=['GET'])
def login():
    login_response = start_login(request, {})
    return make_response(login_response['body'],
                         login_response['statusCode'],
                         login_response['headers'])


@app.route('/finish_login')
def finish():
    finish_login_response = finish_login(request, {})
    return make_response(finish_login_response['body'],
                         finish_login_response['statusCode'],
                         finish_login_response['headers'])
