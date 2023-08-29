from flask import Flask, request
from botutils import Config
import requests

base_url = "http://127.0.0.1:5700/"
app = Flask(__name__)

@app.route('/', methods=["POST"])
def mainHandler():
    data = request.get_json()
    if data['post_type'] == 'meta_event':
        if data['meta_event_type'] == 'heartbeat':
            return 'ok'
    elif data['post_type'] == 'message':
        # messageHandler(data)
        pass
    
    print(data)
    # if data['message'] == 'ping':
    #     requests.get(base_url + 'send_msg', params={'group_id': data['group_id'], 'message': 'pong'})
    return 'ok'
        
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=Config.FLASK_RUN_PORT, debug=True)
