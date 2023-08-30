import requests, xlrd, os
from botutils import Config

class XlKWReply:
    def __init__(self, kdocs_id: str):
        self.kdocs_id = kdocs_id
        self.save_path = "cache/XlKWReply/" + self.kdocs_id + ".xls"
        if not os.path.exists(os.path.dirname(self.save_path)):
            os.makedirs(os.path.dirname(self.save_path))
            self.downxls()
        self.readxls()
            
    def check(self, data):
        key = data['message'].replace('％','%')
        if key == '%reload':
            self.reload()
        elif key in self.kvdict:
            self.send(self.kvdict[key], data)

    def reload(self):
        self.downxls()
        self.readxls()
    
    def downxls(self):
        api_url = "https://www.kdocs.cn/api/office/file/" + self.kdocs_id + "/download"
        dl_url = requests.get(api_url).json().get('download_url')
        xls = requests.get(dl_url)
        with open(self.save_path, 'wb') as f:
            f.write(xls.content)
            
    def readxls(self):
        mainSheet = xlrd.open_workbook(self.save_path).sheets()[0]
        key_list = mainSheet.col_values(0)[1:]
        value_list = mainSheet.col_values(1)[1:]
        self.kvdict = dict(zip(key_list, value_list))
    
    def send(self, content, data):
        if data['message_type'] == 'group':
            requests.get(Config.baseurl + 'send_msg',
                         params={'group_id': data['group_id'],
                                 'message': content})