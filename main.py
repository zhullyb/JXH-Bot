from flask import Flask, request
from botutils import Config
import requests
from MessageHandler import messageHandler

app = Flask(__name__)

@app.route('/', methods=["POST"])
def mainHandler():
    data = request.get_json()
    if data['post_type'] == 'meta_event':
        if data['meta_event_type'] == 'heartbeat':
            return 'ok'
    elif data['post_type'] == 'message':
        messageHandler(data)
    
    print(data)
    # if data['message'] == 'ping':
    #     requests.get(Config.base_url + 'send_msg', params={'group_id': data['group_id'], 'message': 'pong'})
    return 'ok'
        
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=Config.FLASK_RUN_PORT, debug=True)
