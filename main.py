from flask import Flask, request
import requests

base_url = "http://127.0.0.1:5700/"
app = Flask(__name__)

@app.route('/', methods=["POST"])
def post_data():
    data = request.get_json()
    if data['message'] == 'ping':
        requests.get(base_url + 'send_msg', params={'group_id': data['group_id'], 'message': 'pong'})
        
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5701)
